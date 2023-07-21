from pyrogram import *
from pyrogram.types import *
from DzThumbnailBot import Dz
from DzThumbnailBot.core.data import *
from DzThumbnailBot.core.button import *

@Dz.on_callback_query()
async def callback(Dz: Client, query: CallbackQuery):
  data = query.data
  if data == "home":
    await query.message.edit_text(
      text=START_TXT.format(
        query.from_user.first_name,
        BOT_NAME),
      reply_markup=BSTART,
      parse_mode=ParseMode.MARKDOWN,
      disable_web_page_preview=False
      ) 
  elif data == "tutor":
      await query.message.edit_text(
            text=TUTOR_TXT,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=BTUTOR
            )
