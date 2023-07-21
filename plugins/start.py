from pyrogram import *
from pyrogram.types import *
from pyrogram.enums import *
from Database.database import *

from plugins.fsub import *

@Dz.on_message(filters.command("start") & filters.private & sub & sub2)
async def start_cmd(dz: Client, m: Message):
  id = m.from_user.id
  if not await cek_user(id):
    try:
        await add_user(id)
      except:
        pass
   await m.reply_text(
     text=START_TXT.format(tag=
  
