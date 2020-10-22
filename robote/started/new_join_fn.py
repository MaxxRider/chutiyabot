#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
LOGGER=logging.getLogger(__name__)
import pyrogram
from robote import(AUTH_CHANNEL)
async def new_join_f(client,message):
 chat_type=message.chat.type
 if chat_type!="private":
  await message.reply_text(f"Current CHAT ID: <code>{message.chat.id}</code>")
  await client.leave_chat(chat_id=message.chat.id,delete=True)
 await message.delete(revoke=True)
async def help_message_f(client,message):
 await message.reply_text("""""",disable_web_page_preview=True)
async def rename_message_f(client,message):
 inline_keyboard=[]
 inline_keyboard.append([pyrogram.InlineKeyboardButton(text="read this?",url="https://t.me/")])
 reply_markup=pyrogram.InlineKeyboardMarkup(inline_keyboard)
 await message.reply_text("please use @renamebot",quote=True,reply_markup=reply_markup)