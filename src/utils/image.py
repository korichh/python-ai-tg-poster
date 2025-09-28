from pathlib import Path

import requests
from aiogram import Bot

from local_types import ErrorType

from .logger import logger


class ImageUtils:
    images_dir = Path("public") / "images"

    @staticmethod
    def _ensure_images_dir() -> None:
        ImageUtils.images_dir.mkdir(parents=True, exist_ok=True)

    @staticmethod
    async def save_telegram_image(
        bot: Bot, photo_id: str | None, image_name: str
    ) -> str | None:
        try:
            ImageUtils._ensure_images_dir()

            if photo_id is None:
                return None

            image_path = ImageUtils.images_dir / f"{image_name}.jpg"

            await bot.download(photo_id, image_path)

            return str(image_path)

        except Exception as exc:
            logger.error(f"{ErrorType.IMAGE_UTILS_ERROR.value}: {str(exc)}")

            return None

    @staticmethod
    def save_llm_image(image_url: str, image_name: str) -> str | None:
        try:
            ImageUtils._ensure_images_dir()

            image_path = ImageUtils.images_dir / f"{image_name}.png"

            response = requests.get(image_url)
            response.raise_for_status()

            with open(image_path, "wb") as f:
                f.write(response.content)

            return str(image_path)

        except Exception as exc:
            logger.error(f"{ErrorType.IMAGE_UTILS_ERROR.value}: {str(exc)}")

            return None
