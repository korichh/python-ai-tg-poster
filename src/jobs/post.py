from datetime import datetime

from local_types import ErrorType
from services import PostService
from utils import logger


class PostJob:
    @staticmethod
    def publish_analytics_post() -> None:
        try:
            created_at = datetime.now()
            date = created_at.strftime("%Y-%m-%d %H:%M:%S")
            image_name = created_at.strftime("%Y-%m-%d_%H-%M-%S")

            text, image_url = PostService.create_analytics_post()

            pass

        except Exception as exc:
            logger.error(f"{ErrorType.POST_JOB_ERROR}: {str(exc)}")

            return None

    @staticmethod
    def publish_news_meme_post() -> None:
        try:
            pass

        except Exception as exc:
            logger.error(f"{ErrorType.POST_JOB_ERROR}: {str(exc)}")

            return None
