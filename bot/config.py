import os
from dotenv import load_dotenv

load_dotenv()

# Configuration settings
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
