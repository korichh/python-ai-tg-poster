from config import POST
from llms import ImageLlm, TextLlm
from local_types import ErrorType, PostTopic
from utils import logger


class PostService:
    @staticmethod
    def create_post(context: str, post_topic: PostTopic) -> tuple[str, str] | None:
        try:
            topic_config = POST[post_topic]
            topic_text = topic_config["text"]
            topic_image = topic_config["image"]

            text = TextLlm.invoke(context, topic_text)
            image_url = ImageLlm.invoke(topic_image)

            return text, image_url

        except Exception as exc:
            logger.error(f"{ErrorType.POST_SERVICE_ERROR.value}: {str(exc)}")

            return None

    @staticmethod
    def create_analytics_post() -> tuple[str, str] | None:
        try:
            context = "Empty Context"

            text, image_url = PostService.create_post(context, "analytics")

            return text, image_url

        except Exception as exc:
            logger.error(f"{ErrorType.POST_SERVICE_ERROR.value}: {str(exc)}")

            return None

    @staticmethod
    def create_news_post() -> tuple[str, str] | None:
        try:
            context = "Empty Context"

            text, image_url = PostService.create_post(context, "news")

            return text, image_url

        except Exception as exc:
            logger.error(f"{ErrorType.POST_SERVICE_ERROR.value}: {str(exc)}")

            return None

    @staticmethod
    def create_meme_post() -> tuple[str, str] | None:
        try:
            context = "Empty Context"

            text, image_url = PostService.create_post(context, "meme")

            return text, image_url

        except Exception as exc:
            logger.error(f"{ErrorType.POST_SERVICE_ERROR.value}: {str(exc)}")

            return None
