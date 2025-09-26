from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper

from config import llmConfig
from constants import ENV
from local_types import ErrorType
from utils import logger


class ImageChain:
    config = llmConfig["image"]

    llm = DallEAPIWrapper(
        model=config["model"],
        size=config["size"],
        quality=config["quality"],
        api_key=ENV["OPENAI_API_KEY"],
    )

    @staticmethod
    def invoke(topic_image: str) -> str | None:
        try:
            return ImageChain.llm.run(topic_image)

        except Exception as exc:
            logger.error(f"{ErrorType.IMAGE_LLM_ERROR.value}: {str(exc)}")

            return None
