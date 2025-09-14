import os

from dotenv import load_dotenv

load_dotenv()

ENV = {
    "openai_api_key": os.getenv("OPENAI_API_KEY", ""),
    "telegram_bot_token": os.getenv("TELEGRAM_BOT_TOKEN", ""),
    "telegram_channel_id": os.getenv("TELEGRAM_CHANNEL_ID", ""),
}
