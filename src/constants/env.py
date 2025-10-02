import os

from dotenv import load_dotenv

load_dotenv()

ENV = {
    "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY", ""),
    "TELEGRAM_BOT_TOKEN": os.getenv("TELEGRAM_BOT_TOKEN", ""),
    "TELEGRAM_CHANNEL_ID": os.getenv("TELEGRAM_CHANNEL_ID", ""),
    "COINDESK_BASE_URL": os.getenv("COINDESK_BASE_URL", ""),
    "COINDESK_API_KEY": os.getenv("COINDESK_API_KEY", ""),
}
