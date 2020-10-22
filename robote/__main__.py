#!/usr/bin/env python3

# - * -coding: utf - 8 - * -
import os
import io
import sys
import traceback

from robote import(DOWNLOAD_LOCATION, TEGE_TOKEN, TEGE_API_ID, TEGE_API_HASH, AUTH_CHANNEL, LEECH_COMMAND, YTDL_COMMAND, GLEECH_COMMAND, TELEGRAM_LEECH_COMMAND_G, CANCEL_COMMAND_G, GET_SIZE_G, STATUS_COMMAND, SAVE_THUMBNAIL, CLEAR_THUMBNAIL, PYTDL_COMMAND_G, LOG_COMMAND)
from pyrogram import Client, Filters, MessageHandler, CallbackQueryHandler
from robote.started.new_join_fn import new_join_f, help_message_f, rename_message_f
from robote.started.incoming_message_fn import incoming_message_f, incoming_youtube_dl_f, incoming_purge_message_f, incoming_gdrive_message_f, g_yt_playlist
from robote.started.memek_size import check_size_g, g_clearme
from robote.started.status_message_fn import(status_message_f, cancel_message_f, exec_message_f, upload_document_f, upload_log_file)
from robote.started.callback_btn_handler import button
from robote.started.thumbnail_video import(save_thumb_nail, clear_thumb_nail)
from robote.heroku.download import down_load_media_f

if __name__ == "__main__":
  if not os.path.isdir(DOWNLOAD_LOCATION):
    os.makedirs(DOWNLOAD_LOCATION)
  app = Client(
    "robote_lokal",
    bot_token = TEGE_TOKEN,
    api_id = TEGE_API_ID,
    api_hash = TEGE_API_HASH
  )

  callback_btn_handler = CallbackQueryHandler(button)
  app.add_handler(callback_btn_handler)
  cancel_message_handler = MessageHandler(cancel_message_f, filters = Filters.command([f"{CANCEL_COMMAND_G}"]) & Filters.chat(chats = AUTH_CHANNEL))
  app.add_handler(cancel_message_handler)
  clear_thumb_nail_handler = MessageHandler(clear_thumb_nail, filters = Filters.command([f"{CLEAR_THUMBNAIL}"]) & Filters.chat(chats = AUTH_CHANNEL))
  app.add_handler(clear_thumb_nail_handler)
  exec_message_handler = MessageHandler(exec_message_f, filters = Filters.command(["exec"]) & Filters.chat(chats = AUTH_CHANNEL))
  app.add_handler(exec_message_handler)
  group_new_join_handler = MessageHandler(help_message_f, filters = Filters.chat(chats = AUTH_CHANNEL) & Filters.new_chat_members)
  app.add_handler(group_new_join_handler)
  help_text_handler = MessageHandler(help_message_f, filters = Filters.command(["help"]) & Filters.chat(chats = AUTH_CHANNEL))
  app.add_handler(help_text_handler)
  incoming_g_clear_handler = MessageHandler(g_clearme, filters = Filters.command(["renewme"]) & Filters.chat(chats = AUTH_CHANNEL))
  app.add_handler(incoming_g_clear_handler)
  incoming_gdrive_message_handler = MessageHandler(incoming_gdrive_message_f, filters = Filters.command([f"{GLEECH_COMMAND}"]) & Filters.chat(chats = AUTH_CHANNEL))
  app.add_handler(incoming_gdrive_message_handler)
  incoming_message_handler = MessageHandler(incoming_message_f, filters = Filters.command([f"{LEECH_COMMAND}"]) & Filters.chat(chats = AUTH_CHANNEL))
  app.add_handler(incoming_message_handler)
  incoming_purge_message_handler = MessageHandler(incoming_purge_message_f, filters = Filters.command(["purge"]) & Filters.chat(chats = AUTH_CHANNEL))
  app.add_handler(incoming_purge_message_handler)
  incoming_size_checker_handler = MessageHandler(check_size_g, filters = Filters.command([f"{GET_SIZE_G}"]) & Filters.chat(chats = AUTH_CHANNEL))
  app.add_handler(incoming_size_checker_handler)
  incoming_telegram_download_handler = MessageHandler(down_load_media_f, filters = Filters.command([f"{TELEGRAM_LEECH_COMMAND_G}"]) & Filters.chat(chats = AUTH_CHANNEL))
  app.add_handler(incoming_telegram_download_handler)
  incoming_youtube_dl_handler = MessageHandler(incoming_youtube_dl_f, filters = Filters.command([f"{YTDL_COMMAND}"]) & Filters.chat(chats = AUTH_CHANNEL))
  app.add_handler(incoming_youtube_dl_handler)
  incoming_youtube_playlist_dl_handler = MessageHandler(g_yt_playlist, filters = Filters.command([f"{PYTDL_COMMAND_G}"]) & Filters.chat(chats = AUTH_CHANNEL))
  app.add_handler(incoming_youtube_playlist_dl_handler)
  new_join_handler = MessageHandler(new_join_f, filters = ~Filters.chat(chats = AUTH_CHANNEL))
  app.add_handler(new_join_handler)
  rename_message_handler = MessageHandler(rename_message_f, filters = Filters.command(["rename@hahahahahaha"]) & Filters.chat(chats = AUTH_CHANNEL))
  app.add_handler(rename_message_handler)
  save_thumb_nail_handler = MessageHandler(save_thumb_nail, filters = Filters.command([f"{SAVE_THUMBNAIL}"]) & Filters.chat(chats = AUTH_CHANNEL))
  app.add_handler(save_thumb_nail_handler)
  status_message_handler = MessageHandler(status_message_f, filters = Filters.command([f"{STATUS_COMMAND}"]) & Filters.chat(chats = AUTH_CHANNEL))
  app.add_handler(status_message_handler)
  upload_document_handler = MessageHandler(upload_document_f, filters = Filters.command(["upload"]) & Filters.chat(chats = AUTH_CHANNEL))
  app.add_handler(upload_document_handler)
  upload_log_handler = MessageHandler(upload_log_file, filters = Filters.command([f"{LOG_COMMAND}"]) & Filters.chat(chats = AUTH_CHANNEL))
  app.add_handler(upload_log_handler)
  app.run()
