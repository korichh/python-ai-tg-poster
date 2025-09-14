import random
from datetime import datetime

from aiogram import Bot

from local_types import ErrorType
from repositories import PostRepository
from services import PostService
from utils import ImageUtils, logger


class PostJob:
    @staticmethod
    async def publish_analytics_post(bot: Bot) -> None:
        try:
            created_at = datetime.now()
            date = created_at.strftime("%Y-%m-%d %H:%M:%S")
            image_name = created_at.strftime("%Y-%m-%d_%H-%M-%S")

            text, image_url = PostService.create_analytics_post()

            image_path = ImageUtils.save_llm_image(image_url, image_name)

            # await ChannelService.publish_post(text, image_path)

            await PostRepository.add_post(date, text, image_path)

            logger.info("New 'analytics' post published to the channel")

        except Exception as exc:
            logger.error(f"{ErrorType.POST_JOB_ERROR.value}: {str(exc)}")

            return None

    @staticmethod
    async def publish_news_meme_post(bot: Bot) -> None:
        try:
            created_at = datetime.now()
            date = created_at.strftime("%Y-%m-%d %H:%M:%S")
            image_name = created_at.strftime("%Y-%m-%d_%H-%M-%S")

            post_topic = random.choice(["news", "meme"])

            if post_topic == "news":
                text, image_url = PostService.create_news_post()
            else:
                text, image_url = PostService.create_meme_post()

            image_path = ImageUtils.save_llm_image(image_url, image_name)

            # await ChannelService.publish_post(text, image_path)

            await PostRepository.add_post(date, text, image_path)

            logger.info(f"New '{post_topic}' post published to the channel")

        except Exception as exc:
            logger.error(f"{ErrorType.POST_JOB_ERROR.value}: {str(exc)}")

            return None
