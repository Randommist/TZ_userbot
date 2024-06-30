from os import getenv
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_API_ID = getenv("TELEGRAM_API_ID")
if TELEGRAM_API_ID is None:
    raise ValueError("TELEGRAM_API_ID is not set")
TELEGRAM_API_ID = TELEGRAM_API_ID

TELEGRAM_API_HASH = getenv("TELEGRAM_API_HASH")
if TELEGRAM_API_HASH is None:
    raise ValueError("TELEGRAM_API_HASH is not set")
TELEGRAM_API_HASH = TELEGRAM_API_HASH

GSHEET_URL = getenv("GSHEET_URL")
if GSHEET_URL is None:
    raise ValueError("GSHEET_URL is not set")
GSHEET_URL = GSHEET_URL
