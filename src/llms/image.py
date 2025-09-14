from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper

from config import LLM
from constants import ENV
from local_types import ErrorType
from utils import logger


class ImageLlm:
    config = LLM["image"]

    llm = DallEAPIWrapper(
        model=config["model"],
        size=config["size"],
        quality=config["quality"],
        api_key=ENV["openai_api_key"],
    )

    @staticmethod
    def invoke(topic_image: str) -> str | None:
        try:
            return ImageLlm.llm.run(topic_image)

        except Exception as exc:
            logger.error(f"{ErrorType.IMAGE_LLM_ERROR.value}: {str(exc)}")

            return None
