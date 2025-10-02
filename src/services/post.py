from ai import ImageChain, TextChain
from config import postConfig
from local_types import ErrorType, PostTopic
from utils import logger


class PostService:
    @staticmethod
    def create_post(context: str, post_topic: PostTopic) -> tuple[str, str] | None:
        try:
            topic_config = postConfig[post_topic]
            topic_text = topic_config["text"]
            topic_image = topic_config["image"]

            text = TextChain.invoke(context, topic_text)
            image_url = ImageChain.invoke(topic_image)

            return text, image_url

        except Exception as exc:
            logger.error(f"{ErrorType.POST_SERVICE_ERROR.value}: {str(exc)}")

            return None

    @staticmethod
    def create_analytics_post() -> tuple[str, str] | None:
        try:
            context = "Write about BTCUSD, SOLUSD and ETHUSD"

            post = PostService.create_post(context, "analytics")

            if post is None:
                return None

            text, image_url = post

            return text, image_url

        except Exception as exc:
            logger.error(f"{ErrorType.POST_SERVICE_ERROR.value}: {str(exc)}")

            return None

    @staticmethod
    def create_news_post() -> tuple[str, str] | None:
        try:
            context = "Write about BTCUSD, SOLUSD and ETHUSD"

            post = PostService.create_post(context, "news")

            if post is None:
                return None

            text, image_url = post

            return text, image_url

        except Exception as exc:
            logger.error(f"{ErrorType.POST_SERVICE_ERROR.value}: {str(exc)}")

            return None

    @staticmethod
    def create_meme_post() -> tuple[str, str] | None:
        try:
            context = "Write about BTCUSD, SOLUSD and ETHUSD"

            post = PostService.create_post(context, "meme")

            if post is None:
                return None

            text, image_url = post

            return text, image_url

        except Exception as exc:
            logger.error(f"{ErrorType.POST_SERVICE_ERROR.value}: {str(exc)}")

            return None
