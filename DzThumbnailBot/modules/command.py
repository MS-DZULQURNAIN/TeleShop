from pyrogram import *
from pyrogram.types import *
from pyrogram.enums import *
from DzThumbnailBot.core.Database import *
from DzThumbnailBot.core.button import *

@Dz.on_message(filters.command("start") & filters.private & sub & sub2)
async def start_cmd(dz: Client, m: Message):
  first = m.from_user.first_name
  last = m.from_user.last_name
  id = m.from_user.id
  if not await cek_user(id):
    try:
        await add_user(id)
      except:
        pass
   await m.reply_text(
     text=START_TXT.format(first, last, id),
     reply_markup=BSTART,
     parse_mode=ParseMode.MARKDOWN,
     disable_web_page_preview=False
     )

@Dz.on_message(filters.command("help") & filters.private)
async def help_cmd(dz: Client, m: Message):
  await m.reply_text(
    text=HELP_TXT, 
    parse_mode=ParseMode.MARKDOWN,
    reply_markup=BHELP,
    disable_web_page_preview=False
    )
