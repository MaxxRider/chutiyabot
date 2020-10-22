#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
LOGGER=logging.getLogger(__name__)
import asyncio
import os
import time
from robote.lokal.copy_similar_file import copy_file
async def take_screen_shot(video_file,output_directory,ttl):
 out_put_file_name=os.path.join(output_directory,str(time.time())+".jpg")
 if video_file.upper().endswith(("MKV","MP4","M4V","AVI","WEBM")):
  file_genertor_command=["ffmpeg","-ss",str(ttl),"-i",video_file,"-vframes","1",out_put_file_name]
  process=await asyncio.create_subprocess_exec(*file_genertor_command,stdout=asyncio.subprocess.PIPE,stderr=asyncio.subprocess.PIPE,)
  stdout,stderr=await process.communicate()
  e_response=stderr.decode().strip()
  t_response=stdout.decode().strip()
 if os.path.lexists(out_put_file_name):
  return out_put_file_name
 else:
  return None
