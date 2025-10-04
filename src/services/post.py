from ai import ImageChain, TextChain
from config import postConfig
from local_types import ErrorType, PostTopic
from services import CoindeskService
from utils import format_analytics_context, format_news_context, logger


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
    async def create_analytics_post() -> tuple[str, str] | None:
        try:
            coins = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]

            metadata = await CoindeskService.get_instruments_metadata(coins)
            latest_tick = await CoindeskService.get_instruments_latest_tick(coins)
            historical_prices = await CoindeskService.get_instruments_historical_prices(
                coins
            )

            context = format_analytics_context(
                coins, metadata, latest_tick, historical_prices
            )

            post = PostService.create_post(context, "analytics")

            if post is None:
                return None

            text, image_url = post

            return text, image_url

        except Exception as exc:
            logger.error(f"{ErrorType.POST_SERVICE_ERROR.value}: {str(exc)}")

            return None

    @staticmethod
    async def create_news_post() -> tuple[str, str] | None:
        try:
            coins = ["Bitcoin crypto", "Ethereum crypto", "Solana crypto"]

            news = await CoindeskService.get_instruments_news(coins)

            context = format_news_context(news)

            post = PostService.create_post(context, "news")

            if post is None:
                return None

            text, image_url = post

            return text, image_url

        except Exception as exc:
            logger.error(f"{ErrorType.POST_SERVICE_ERROR.value}: {str(exc)}")

            return None

    @staticmethod
    async def create_meme_post() -> tuple[str, str] | None:
        try:
            post = PostService.create_post("Trading", "meme")

            if post is None:
                return None

            text, image_url = post

            return text, image_url

        except Exception as exc:
            logger.error(f"{ErrorType.POST_SERVICE_ERROR.value}: {str(exc)}")

            return None
