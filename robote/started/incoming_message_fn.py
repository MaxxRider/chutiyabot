#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
LOGGER=logging.getLogger(__name__)
import os
import requests
from robote import(DOWNLOAD_LOCATION)
import time
import aria2p
import asyncio
from robote.lokal.extract_link_from_message import extract_link
from robote.heroku.download_wariya import call_apropriate_function,call_apropriate_function_g,aria_start
from robote.heroku.download_link import request_download
from robote.lokal.display_progress import progress_for_pyrogram
from robote.lokal.youtube_dl_extractor import extract_youtube_dl_formats
from robote.lokal.admin_check import AdminCheck
from robote.lokal.ytplaylist import yt_playlist_downg
async def incoming_purge_message_f(client,message):
 i_m_sefg2=await message.reply_text("Purging...",quote=True)
 if await AdminCheck(client,message.chat.id,message.from_user.id):
  aria_i_p=await aria_start()
  downloads=aria_i_p.get_downloads()
  for download in downloads:
   LOGGER.info(download.remove(force=True))
 await i_m_sefg2.delete()
async def incoming_message_f(client,message):
 i_m_sefg=await message.reply_text("processing",quote=True)
 is_zip=False
 is_unzip=False
 is_unrar=False
 is_untar=False
 if len(message.command)>1:
  if message.command[1]=="archive":
   is_zip=True
  elif message.command[1]=="unzip":
   is_unzip=True
  elif message.command[1]=="unrar":
   is_unrar=True
  elif message.command[1]=="untar":
   is_untar=True
 dl_url,cf_name,_,_=await extract_link(message.reply_to_message,"LEECH")
 LOGGER.info(dl_url)
 LOGGER.info(cf_name)
 if dl_url is not None:
  await i_m_sefg.edit_text("extracting links")
  aria_i_p=await aria_start()
  LOGGER.info(aria_i_p)
  current_user_id=message.from_user.id
  new_download_location=os.path.join(DOWNLOAD_LOCATION,str(current_user_id),str(time.time()))
  if not os.path.isdir(new_download_location):
   os.makedirs(new_download_location)
  await i_m_sefg.edit_text("trying to download")
  sagtus,err_message=await call_apropriate_function(aria_i_p,dl_url,new_download_location,i_m_sefg,is_zip,cf_name,is_unzip,is_unrar,is_untar,message)
  if not sagtus:
   await i_m_sefg.edit_text(err_message)
 else:
  await i_m_sefg.edit_text("**FCUK**! wat have you entered. \nPlease read /help \n" f"<b>API Error</b>: {cf_name}")
async def incoming_gdrive_message_f(client,message):
 i_m_sefg=await message.reply_text("processing",quote=True)
 is_zip=False
 is_unzip=False
 is_unrar=False
 is_untar=False
 if len(message.command)>1:
  if message.command[1]=="archive":
   is_zip=True
  elif message.command[1]=="unzip":
   is_unzip=True
  elif message.command[1]=="unrar":
   is_unrar=True
  elif message.command[1]=="untar":
   is_untar=True
 dl_url,cf_name,_,_=await extract_link(message.reply_to_message,"GLEECH")
 LOGGER.info(dl_url)
 LOGGER.info(cf_name)
 if dl_url is not None:
  await i_m_sefg.edit_text("extracting links")
  aria_i_p=await aria_start()
  LOGGER.info(aria_i_p)
  current_user_id=message.from_user.id
  new_download_location=os.path.join(DOWNLOAD_LOCATION,str(current_user_id),str(time.time()))
  if not os.path.isdir(new_download_location):
   os.makedirs(new_download_location)
  await i_m_sefg.edit_text("trying to download")
  await call_apropriate_function_g(aria_i_p,dl_url,new_download_location,i_m_sefg,is_zip,cf_name,is_unzip,is_unrar,is_untar,message)
 else:
  await i_m_sefg.edit_text("**FCUK**! wat have you entered. \nPlease read /help \n" f"<b>API Error</b>: {cf_name}")
async def incoming_youtube_dl_f(client,message):
 i_m_sefg=await message.reply_text("processing",quote=True)
 dl_url,cf_name,yt_dl_user_name,yt_dl_pass_word=await extract_link(message.reply_to_message,"YTDL")
 LOGGER.info(dl_url)
 LOGGER.info(cf_name)
 if dl_url is not None:
  await i_m_sefg.edit_text("extracting links")
  current_user_id=message.from_user.id
  user_working_dir=os.path.join(DOWNLOAD_LOCATION,str(current_user_id))
  if not os.path.isdir(user_working_dir):
   os.makedirs(user_working_dir)
  thumb_image,text_message,reply_markup=await extract_youtube_dl_formats(dl_url,cf_name,yt_dl_user_name,yt_dl_pass_word,user_working_dir)
  print(thumb_image)
  req=requests.get(f"{thumb_image}")
  gau_tam=f"{current_user_id}.jpg"
  open(gau_tam,'wb').write(req.content)
  if thumb_image is not None:
   await message.reply_photo(photo=gau_tam,quote=True,caption=text_message,reply_markup=reply_markup)
   await i_m_sefg.delete()
  else:
   await i_m_sefg.edit_text(text=text_message,reply_markup=reply_markup)
 else:
  await i_m_sefg.edit_text("**FCUK**! wat have you entered. \nPlease read /help \n" f"<b>API Error</b>: {cf_name}")
async def g_yt_playlist(client,message):
 usr_id=message.from_user.id
 G_DRIVE=False
 if len(message.command)>1:
  if message.command[1]=="gdrive":
   G_DRIVE=True
 if 'youtube.com/playlist' in message.reply_to_message.text:
  i_m_sefg=await message.reply_text("Downloading...you should wait🤗",quote=True)
  await yt_playlist_downg(message.reply_to_message,i_m_sefg,G_DRIVE)
 else:
  await message.reply_text("Reply to youtube playlist link only 🙄")