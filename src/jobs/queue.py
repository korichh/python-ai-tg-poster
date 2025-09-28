from datetime import datetime

from aiogram import Bot

from local_types import ErrorType
from repositories import PostRepository, QueueRepository
from services import ChannelService
from utils import ImageUtils, logger


class QueueJob:
    @staticmethod
    async def publish_queue_post(bot: Bot) -> None:
        try:
            created_at = datetime.now()
            date = created_at.strftime("%Y-%m-%d %H:%M:%S")
            image_name = created_at.strftime("%Y-%m-%d_%H-%M-%S")

            post = await QueueRepository.pop_post()

            if post is None:
                return None

            image_path = await ImageUtils.save_telegram_image(
                bot, post["photo_id"], image_name
            )

            await ChannelService.publish_post(bot, post["text"], image_path)

            await PostRepository.add_post(date, post["text"], image_path)

            logger.info("New post from the queue published to the channel")

        except Exception as exc:
            logger.error(f"{ErrorType.QUEUE_JOB_ERROR.value}: {str(exc)}")

            return None
