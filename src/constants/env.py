import os

from dotenv import load_dotenv

load_dotenv()

ENV = {
    "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY", ""),
    "TELEGRAM_BOT_TOKEN": os.getenv("TELEGRAM_BOT_TOKEN", ""),
    "TELEGRAM_CHANNEL_ID": os.getenv("TELEGRAM_CHANNEL_ID", ""),
}
