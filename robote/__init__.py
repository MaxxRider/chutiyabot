#!/usr/bin/env python3

# - * -coding: utf - 8 - * -
import os
import time
if bool(os.environ.get("ENV", False)):
  from robote.dev_config import Config
else :
  from robote.config import Config

TEGE_TOKEN = Config.TEGE_TOKEN
TEGE_API_ID = Config.TEGE_API_ID
TEGE_API_HASH = Config.TEGE_API_HASH
TEGE_OWNER = Config.TEGE_OWNER
ARIATWO_PORT = Config.ARIATWO_PORT
AUTH_CHANNEL = list(Config.AUTH_CHANNEL)
AUTH_CHANNEL = list(set(AUTH_CHANNEL))
AUTH_CHANNEL.append(TEGE_OWNER)
BOT_START_TIME = time.time()
CANCEL_COMMAND_G = Config.CANCEL_COMMAND_G
CHUNK_SIZE = Config.CHUNK_SIZE
CLEAR_THUMBNAIL = Config.CLEAR_THUMBNAIL
CUSTOM_FILE_NAME = Config.CUSTOM_FILE_NAME
DEF_THUMB_NAIL_VID_S = Config.DEF_THUMB_NAIL_VID_S
DESTINATION_FOLDER = Config.DESTINATION_FOLDER
DOWNLOAD_LOCATION = Config.DOWNLOAD_LOCATION
EDIT_SLEEP_TIME_OUT = Config.EDIT_SLEEP_TIME_OUT
FINISHED_PROGRESS_STR = Config.FINISHED_PROGRESS_STR
FREE_USER_MAX_FILE_SIZE = Config.FREE_USER_MAX_FILE_SIZE
GET_SIZE_G = Config.GET_SIZE_G
GLEECH_COMMAND = Config.GLEECH_COMMAND
INDEX_LINK = Config.INDEX_LINK
LEECH_COMMAND = Config.LEECH_COMMAND
LOG_COMMAND = Config.LOG_COMMAND
MAX_FILE_SIZE = Config.MAX_FILE_SIZE
MAX_MESSAGE_LENGTH = Config.MAX_MESSAGE_LENGTH
MAX_TG_SPLIT_FILE_SIZE = Config.MAX_TG_SPLIT_FILE_SIZE
MAX_TIME_WAIT_TORRENTS_START = Config.MAX_TIME_WAIT_TORRENTS_START
PROCESS_MAX_TIMEOUT = Config.PROCESS_MAX_TIMEOUT
PYTDL_COMMAND_G = Config.PYTDL_COMMAND_G
UPLOADER_CONFIG = Config.UPLOADER_CONFIG
SAVE_THUMBNAIL = Config.SAVE_THUMBNAIL
STATUS_COMMAND = Config.STATUS_COMMAND
TELEGRAM_LEECH_COMMAND_G = Config.TELEGRAM_LEECH_COMMAND_G
TG_MAX_FILE_SIZE = Config.TG_MAX_FILE_SIZE
TG_OFFENSIVE_API = Config.TG_OFFENSIVE_API
UN_FINISHED_PROGRESS_STR = Config.UN_FINISHED_PROGRESS_STR
UPLOAD_AS_DOC = Config.UPLOAD_AS_DOC
YTDL_COMMAND = Config.YTDL_COMMAND

if os.path.exists("robote.log"):
  with open("robote.log", "r+") as f_d:
    f_d.truncate(0)

import base64
import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(level = logging.INFO, format = "%(asctime)s %(message)s", datefmt = "%H:%M:%S", handlers = [RotatingFileHandler("robote.log", maxBytes = FREE_USER_MAX_FILE_SIZE, backupCount = 10), logging.StreamHandler()])
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)
