import logging
from logging.handlers import RotatingFileHandler

LOG_FILE_NAME = "DzThumbnailBot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

#---------- ---------- ---------- ----------
from pyrogram import Client
from DzThumbnailBot.config import API_ID, API_HASH, TOKEN

class Dz(Client):
    def __init__(self):
        super().__init__(
            "bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            bot_token=TOKEN, 
            plugins={
                "root": "DzThumbnailBot/modules"
            }
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        nama_bot = await self.get_me()
        self.LOGGER(__name__).info(f"@{nama_bot.username}  started!")
        self.LOGGER(__name__).info("Created by DezetProject\nhttps://t.me/DezetStore")
        self.bot_details = bot_details

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
