from pyrogram import *
from pyrogram.types import *

BSTART = InlineKeyboardMarkup([
            [
              InlineKeyboardButton(text="Akun Saya", callback_data="my_account"),
            ],
            [
              InlineKeyboardButton(text="Developer👤", url="https://t.me/MSDQQQ"),
            ],
            [
              InlineKeyboardButton(text="Tutorial💡", callback_data="tutor"),
              InlineKeyboardButton(text="Donasi💌", callback_data="donasi"),
            ],
            [
              InlineKeyboardButton(text="Channel", url="https://t.me/DezetStore"),
              InlineKeyboardButton(text="Support", url="https://t.me/DezetSupport"),
            ],
            [
              InlineKeyboardButton(text="Tutup", callback_data="close"),
            ]
       ])

BHOME = InlineKeyboardMarkup([
                   [
                        InlineKeyboardButton("Kembali", callback_data="home")
                   ]
             ])
