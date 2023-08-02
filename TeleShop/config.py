import os
from dotenv import load_dotenv

load_dotenv() 
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
TOKEN = os.environ.get("TOKEN")
OWNER_ID = int(os.environ.get("OWNER_ID"))
LOG = int(os.environ.get("LOG"))
DATABASE_URI = os.environ.get("DATABASE_URI")
BOT_NAME = os.environ.get("BOT_NAME")
