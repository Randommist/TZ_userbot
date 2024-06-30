from pyrogram.client import Client
import gspread

from env import TELEGRAM_API_ID as api_id, TELEGRAM_API_HASH as api_hash, GSHEET_URL
from utils import get_work_dir

app = Client("userbot", api_id, api_hash, workdir=get_work_dir())
gc = gspread.auth.service_account()
worksheet = gc.open_by_url(GSHEET_URL).sheet1
