from pyrogram import *
from pyrogram.types import *
from TeleShop import Dz
from TeleShop.core.data import *
from TeleShop.core.button import *
from TeleShop.Database.database import *

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
  elif data == "my_account":
    namad = query.from_user.first_name
    namab = query.from_user.last_name
    idku = query.from_user.id
    saldoku = {user.data
    await query.message.edit_text(
      text=MY_ACCOUNT.format(namad, namab, idku, saldo, premium, transaksi), 
      parse_mode=ParseMode.MARKDOWN, 
      disable_web_page_preview=False, 
      reply_markup=BHOME, 
      ) 
