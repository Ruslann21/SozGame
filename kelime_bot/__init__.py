from time import sleep
from pyrogram import Client
import logging
from dotenv import load_dotenv, set_key, unset_key
from os import getenv

load_dotenv('config.env')

# THE LOGGING
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)


# Hesap
API_ID = getenv("API_ID", "22007754")
API_HASH = getenv("API_HASH", "7f0d6b4d928155eda014acdb5a014620")
TOKEN = getenv("TOKEN", "6447680335:AAFs4Nnuy0sj7vmQJ1KEkDPs6McjLfTXUHY")
USERNAME = getenv("USERNAME", "smaylw")
OWNER_ID = getenv("OWNER_ID", "6142419734")

if OWNER_ID and len(OWNER_ID) and OWNER_ID.isdigit():
    OWNER_ID = int(OWNER_ID)  # type: ignore
else:
    OWNER_ID = None  # type: ignore

# BOT CLIENTİ
bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=TOKEN,
    plugins=dict(root="kelime_bot/plugins/"),
    workers=16
)


# Oyun Verileri
oyun = {}  # type: ignore


# rating
rating = {}  # type: ignore
