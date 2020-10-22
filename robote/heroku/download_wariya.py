#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
sys.setrecursionlimit(10**6)
LOGGER = logging.getLogger(__name__)

import aria2p
import asyncio
import os
from robote.heroku.upload_tege import upload_tege, upload_to_gdrive
from robote.heroku.create_archive import create_archive, unzip_me, unrar_me, untar_me
from robote.lokal.extract_link_from_message import extract_link
from robote import(ARIATWO_PORT, MAX_TIME_WAIT_TORRENTS_START, AUTH_CHANNEL, DOWNLOAD_LOCATION, EDIT_SLEEP_TIME_OUT, CUSTOM_FILE_NAME)
from pyrogram import(InlineKeyboardButton, InlineKeyboardMarkup, Message)

async def aria_start():
    aria2_daemon_start_cmd = []
    aria2_daemon_start_cmd.append("aria2c")
    aria2_daemon_start_cmd.append("--conf-path=/opt/download.conf")
    aria2_daemon_start_cmd.append(f"--rpc-listen-port={ARIATWO_PORT}")
    LOGGER.info(aria2_daemon_start_cmd)
    process = await asyncio.create_subprocess_exec(
        *aria2_daemon_start_cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    LOGGER.info(stdout or stderr)
    aria2 = aria2p.API(
        aria2p.Client(
            host="http://localhost",
            port=ARIATWO_PORT,
            secret=""
        )
    )
    return aria2


def add_magnet(aria_instance, magnetic_link, c_file_name):
    options = None
    try:
        download = aria_instance.add_magnet(
            magnetic_link,
            options=options
        )
    except Exception as e:
        return False, "**FAILED** \n" + str(e) + " \nPlease do not send SLOW links. Read /help"
    else:
        return True, "" + download.gid + ""


def add_torrent(aria_instance, torrent_file_path):
    if torrent_file_path is None:
        return False, "**FAILED** \n" + str(e) + " \nsomething wrongings when trying to add <u>TORRENT</u> file"
    if os.path.exists(torrent_file_path):
        # Add Torrent Into Queue
        try:
            download = aria_instance.add_torrent(
                torrent_file_path,
                uris=None,
                options=None,
                position=None
            )
        except Exception as e:
            return False, "**FAILED** \n" + str(e) + " \nPlease do not send SLOW links. Read /help"
        else:
            return True, "" + download.gid + ""
    else:
        return False, "**FAILED** \n" + str(e) + " \nPlease try other sources to get workable link"


def add_url(aria_instance, text_url, c_file_name):
    options = None
    uris = [text_url]
    try:
        download = aria_instance.add_uris(
            uris,
            options=options
        )
    except Exception as e:
        return False, "**FAILED** \n" + str(e) + " \nPlease do not send SLOW links. Read /help"
    else:
        return True, "" + download.gid + ""


async def call_apropriate_function(
    aria_instance,
    incoming_link,
    c_file_name,
    sent_message_to_update_tg_p,
    is_zip,
    cstom_file_name,
    is_unzip,
    is_unrar,
    is_untar,
    user_message
):
    if incoming_link.lower().startswith("magnet:"):
        sagtus, err_message = add_magnet(aria_instance, incoming_link, c_file_name)
    elif incoming_link.lower().endswith(".torrent"):
        sagtus, err_message = add_torrent(aria_instance, incoming_link)
    else:
        sagtus, err_message = add_url(aria_instance, incoming_link, c_file_name)
    if not sagtus:
        return sagtus, err_message
    LOGGER.info(err_message)
    await check_progress_for_dl(
        aria_instance,
        err_message,
        sent_message_to_update_tg_p,
        None
    )
    if incoming_link.startswith("magnet:"):
        #
        err_message = await check_metadata(aria_instance, err_message)
        #
        await asyncio.sleep(1)
        if err_message is not None:
            await check_progress_for_dl(
                aria_instance,
                err_message,
                sent_message_to_update_tg_p,
                None
            )
        else:
            return False, "can't get metadata \n\n#stopped"
    await asyncio.sleep(1)
    file = aria_instance.get_download(err_message)
    to_upload_file = file.name
    #
    if is_zip:
        check_if_file = await create_archive(to_upload_file)
        if check_if_file is not None:
            to_upload_file = check_if_file
    #
    if is_unzip:
        check_ifi_file = await unzip_me(to_upload_file)
        if check_ifi_file is not None:
            to_upload_file = check_ifi_file
    #
    if is_unrar:
        check_ife_file = await unrar_me(to_upload_file)
        if check_ife_file is not None:
            to_upload_file = check_ife_file
    #
    if is_untar:
        check_ify_file = await untar_me(to_upload_file)
        if check_ify_file is not None:
            to_upload_file = check_ify_file
    #
    if to_upload_file:
        if CUSTOM_FILE_NAME:
            os.rename(to_upload_file, f"{CUSTOM_FILE_NAME}{to_upload_file}")
            to_upload_file = f"{CUSTOM_FILE_NAME}{to_upload_file}"
        else:
            to_upload_file = to_upload_file

    if cstom_file_name:
        os.rename(to_upload_file, cstom_file_name)
        to_upload_file = cstom_file_name
    else:
        to_upload_file = to_upload_file
    #
    response = {}
    LOGGER.info(response)
    user_id = user_message.from_user.id
    print(user_id)
    final_response = await upload_tege(
        sent_message_to_update_tg_p,
        to_upload_file,
        user_id,
        response
    )
    LOGGER.info(final_response)
    try:
        message_to_send = ""
        for key_f_res_se in final_response:
            local_file_name = key_f_res_se
            message_id = final_response[key_f_res_se]
            channel_id = str(sent_message_to_update_tg_p.chat.id)[4:]
            private_link = f"https://t.me/c/{channel_id}/{message_id}"
            message_to_send += "📃 <a href='"
            message_to_send += private_link
            message_to_send += "'>"
            message_to_send += local_file_name
            message_to_send += "</a>"
            message_to_send += "\n"
        if message_to_send != "":
            mention_req_user = f"<a href='tg://user?id={user_id}'>Files Successfully Downloaded 📁</a>\n\n"
            message_to_send = mention_req_user + message_to_send
            message_to_send = message_to_send + "\n\n" + "#Uploaded\n"
        else:
            message_to_send = "<i>FAILED</i> to upload files. 😞😞"
        await user_message.reply_text(
            text=message_to_send,
            quote=True,
            disable_web_page_preview=True
        )
    except:
        pass
    return True, None
#

async def call_apropriate_function_g(
    aria_instance,
    incoming_link,
    c_file_name,
    sent_message_to_update_tg_p,
    is_zip,
    cstom_file_name,
    is_unzip,
    is_unrar,
    is_untar,
    user_message
):
    if incoming_link.lower().startswith("magnet:"):
        sagtus, err_message = add_magnet(aria_instance, incoming_link, c_file_name)
    elif incoming_link.lower().endswith(".torrent"):
        sagtus, err_message = add_torrent(aria_instance, incoming_link)
    else:
        sagtus, err_message = add_url(aria_instance, incoming_link, c_file_name)
    if not sagtus:
        return sagtus, err_message
    LOGGER.info(err_message)
    await check_progress_for_dl(
        aria_instance,
        err_message,
        sent_message_to_update_tg_p,
        None
    )
    if incoming_link.startswith("magnet:"):
        #
        err_message = await check_metadata(aria_instance, err_message)
        #
        await asyncio.sleep(1)
        if err_message is not None:
            await check_progress_for_dl(
                aria_instance,
                err_message,
                sent_message_to_update_tg_p,
                None
            )
        else:
            return False, "can't get metadata \n\n#stopped"
    await asyncio.sleep(1)
    file = aria_instance.get_download(err_message)
    to_upload_file = file.name
    #
    if is_zip:
        check_if_file = await create_archive(to_upload_file)
        if check_if_file is not None:
            to_upload_file = check_if_file
    #
    if is_unzip:
        check_ifi_file = await unzip_me(to_upload_file)
        if check_ifi_file is not None:
            to_upload_file = check_ifi_file
    #
    if is_unrar:
        check_ife_file = await unrar_me(to_upload_file)
        if check_ife_file is not None:
            to_upload_file = check_ife_file
    #
    if is_untar:
        check_ify_file = await untar_me(to_upload_file)
        if check_ify_file is not None:
            to_upload_file = check_ify_file
    #
    if to_upload_file:
        if CUSTOM_FILE_NAME:
            os.rename(to_upload_file, f"{CUSTOM_FILE_NAME}{to_upload_file}")
            to_upload_file = f"{CUSTOM_FILE_NAME}{to_upload_file}"
        else:
            to_upload_file = to_upload_file

    if cstom_file_name:
        os.rename(to_upload_file, cstom_file_name)
        to_upload_file = cstom_file_name
    else:
        to_upload_file = to_upload_file
    #
    response = {}
    LOGGER.info(response)
    user_id = user_message.from_user.id
    print(user_id)
    final_response = await upload_to_gdrive(
        to_upload_file,
        sent_message_to_update_tg_p,
        user_message,
        user_id
    )
#
async def call_apropriate_function_t(
    to_upload_file_g,
    sent_message_to_update_tg_p,
    is_unzip,
    is_unrar,
    is_untar
):
    #
    to_upload_file = to_upload_file_g
    if is_unzip:
        check_ifi_file = await unzip_me(to_upload_file_g)
        if check_ifi_file is not None:
            to_upload_file = check_ifi_file
    #
    if is_unrar:
        check_ife_file = await unrar_me(to_upload_file_g)
        if check_ife_file is not None:
            to_upload_file = check_ife_file
    #
    if is_untar:
        check_ify_file = await untar_me(to_upload_file_g)
        if check_ify_file is not None:
            to_upload_file = check_ify_file
    #
    response = {}
    LOGGER.info(response)
    user_id = sent_message_to_update_tg_p.reply_to_message.from_user.id
    final_response = await upload_to_gdrive(
        to_upload_file,
        sent_message_to_update_tg_p
    )
    LOGGER.info(final_response)

async def check_progress_for_dl(aria2, gid, event, previous_message):
    try:
        file = aria2.get_download(gid)
        complete = file.is_complete
        is_file = file.seeder
        if not complete:
            if not file.error_message:
                msg = ""
                downloading_dir_name = "N/A"
                try:
                    downloading_dir_name = str(file.name)
                except:
                    pass
                #
                msg = f"\n<b>○📂File:</b> `<code>{downloading_dir_name}</code>`"
                msg += f"\n<b>○Speed:</b> <code>{file.download_speed_string()}🔻|{file.upload_speed_string()}🔺</code>"
                msg += f"\n<b>○Progress:</b> <code>{file.progress_string()}</code>"
                msg += f"\n<b>○Size:</b> <b>{file.total_length_string()}</b>"
 
                if is_file is None :
                   msg += f"\n<b>🔗Connections:</b> {file.connections}"
                else :
                   msg += f"\n<b>◌Peers:</b> <code>{file.connections}</code> || <b>○ Seeders:</b> <code>{file.num_seeders}</code>"

                # msg += f"\n<b>◌Status:</b> {file.status}"
                msg += f"\n<b>◌ETA:</b> {file.eta_string()}"
                msg += f"\n<b>◌GID:</b> <code>{gid}</code>\n"
                inline_keyboard = []
                ikeyboard = []
                ikeyboard.append(InlineKeyboardButton("Cancel downloading ‼️", callback_data=(f"cancel {gid}").encode("UTF-8")))
                inline_keyboard.append(ikeyboard)
                reply_markup = InlineKeyboardMarkup(inline_keyboard)
                #msg += reply_markup
                LOGGER.info(msg)
                if msg != previous_message:
                    await event.edit(msg, reply_markup=reply_markup)
                    previous_message = msg
            else:
                msg = file.error_message
                await asyncio.sleep(EDIT_SLEEP_TIME_OUT)
                await event.edit(f"`{msg}`")
                return False
            await asyncio.sleep(EDIT_SLEEP_TIME_OUT)
            await check_progress_for_dl(aria2, gid, event, previous_message)
        else:
            await asyncio.sleep(EDIT_SLEEP_TIME_OUT)
            await event.edit(f"File Downloaded Successfully: `{file.name}`")
            return True
    except Exception as e:
        LOGGER.info(str(e))
        if " not found" in str(e) or "'file'" in str(e):
            await event.edit("Download Canceled")
            return False
        elif " depth exceeded" in str(e):
            file.remove(force=True)
            await event.edit("Download Auto Canceled\nYour Torrent/Link is Dead.")
            return False
        else:
            LOGGER.info(str(e))
            await event.edit("<u>error</u> :\n`{}` \n\n#error".format(str(e)))
            return


async def check_metadata(aria2, gid):
    file = aria2.get_download(gid)
    LOGGER.info(file)
    if not file.followed_by_ids:
        return None
    new_gid = file.followed_by_ids[0]
    LOGGER.info("Changing GID " + gid + " to " + new_gid)
    return new_gid
