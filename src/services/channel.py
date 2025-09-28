from aiogram import Bot
from aiogram.types import FSInputFile

from constants import ENV
from local_types import ErrorType
from utils import logger


class ChannelService:
    @staticmethod
    async def publish_post(bot: Bot, text: str, image_path: str | None) -> None:
        try:
            if image_path:
                photo = FSInputFile(image_path)

                await bot.send_photo(
                    chat_id=ENV["TELEGRAM_CHANNEL_ID"], photo=photo, caption=text
                )
            else:
                await bot.send_message(chat_id=ENV["TELEGRAM_CHANNEL_ID"], text=text)

        except Exception as exc:
            logger.error(f"{ErrorType.CHANNEL_SERVICE_ERROR.value}: {str(exc)}")

            return None
