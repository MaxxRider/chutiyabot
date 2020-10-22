#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
logger=logging.getLogger(__name__)
import math
import os
import time
from robote import(FINISHED_PROGRESS_STR,UN_FINISHED_PROGRESS_STR,EDIT_SLEEP_TIME_OUT)
async def progress_for_pyrogram_g(current,total,ud_type,message,start):
 now=time.time()
 diff=now-start
 if round(diff%10.00)==0 or current==total:
  percentage=current*100/total
  speed=current/diff
  elapsed_time=round(diff)*1000
  time_to_completion=round((total-current)/speed)*1000
  estimated_total_time=elapsed_time+time_to_completion
  elapsed_time=time_formatter(milliseconds=elapsed_time)
  estimated_total_time=time_formatter(milliseconds=estimated_total_time)
  progress="[{0}{1}] \n<b>◌Progress:</b> <code>〘 {2}% 〙</code>\n◌Completed✓:</b> ".format(''.join([FINISHED_PROGRESS_STR for i in range(math.floor(percentage/12))]),''.join([UN_FINISHED_PROGRESS_STR for i in range(12-math.floor(percentage/12))]),round(percentage,2))
  tmp=progress+"<code>〘 {0} 〙</code>\n<b>◌Total</b> <code>〘 {1} 〙</code>\n<b>◌Speed:</b> <code>〘 {2}/s 〙</code>\n<b>◌ETA:</b> <code>〘 {3} 〙</code>\n\n<b>🛡️ Powered By : @robote_lokal</b>\n".format(humanbytes(current),humanbytes(total),humanbytes(speed),estimated_total_time if estimated_total_time!='' else "0 s")
  try:
   await message.edit("{}\n {}".format(ud_type,tmp))
  except:
   pass
def humanbytes(size:int)->str:
 if not size:
  return ""
 power=2**10
 number=0
 dict_power_n={0:" ",1:"Ki",2:"Mi",3:"Gi",4:"Ti"}
 while size>power:
  size/=power
  number+=1
 return str(round(size,2))+" "+dict_power_n[number]+'B'
def time_formatter(milliseconds:int)->str:
 seconds,milliseconds=divmod(int(milliseconds),1000)
 minutes,seconds=divmod(seconds,60)
 hours,minutes=divmod(minutes,60)
 days,hours=divmod(hours,24)
 tmp=((str(days)+"d, ")if days else "")+ ((str(hours)+"h, ")if hours else "")+ ((str(minutes)+"m, ")if minutes else "")+ ((str(seconds)+"s, ")if seconds else "")+ ((str(milliseconds)+"ms, ")if milliseconds else "")
 return tmp[:-2]
