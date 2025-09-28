import asyncio
import json
from pathlib import Path
from typing import List

from local_types import ErrorType, Post
from utils import logger


class QueueRepository:
    queue_file: Path = Path("database") / "queue.json"
    _lock: asyncio.Lock = asyncio.Lock()

    @staticmethod
    async def _get_queue() -> List[Post]:
        async with QueueRepository._lock:
            try:
                with open(QueueRepository.queue_file, "r", encoding="utf-8") as f:
                    return json.load(f)

            except Exception:
                return []

    @staticmethod
    async def _update_queue(queue: List[Post]) -> None:
        async with QueueRepository._lock:
            with open(QueueRepository.queue_file, "w", encoding="utf-8") as f:
                json.dump(queue, f, indent=2, ensure_ascii=False)

    @staticmethod
    async def _create_queue_file() -> None:
        async with QueueRepository._lock:
            with open(QueueRepository.queue_file, "w", encoding="utf-8") as f:
                json.dump([], f, indent=2, ensure_ascii=False)

    @staticmethod
    async def _ensure_queue_file() -> None:
        QueueRepository.queue_file.parent.mkdir(parents=True, exist_ok=True)

        if not QueueRepository.queue_file.exists():
            await QueueRepository._create_queue_file()

        else:
            try:
                async with QueueRepository._lock:
                    with open(QueueRepository.queue_file, "r", encoding="utf-8") as f:
                        json.load(f)

            except Exception:
                await QueueRepository._create_queue_file()

    @staticmethod
    async def add_post(text: str, photo_id: str | None) -> None:
        try:
            await QueueRepository._ensure_queue_file()

            queue = await QueueRepository._get_queue()
            queue.append({"text": text, "photo_id": photo_id})

            await QueueRepository._update_queue(queue)

        except Exception as exc:
            logger.error(f"{ErrorType.QUEUE_SERVICE_ERROR.value}: {str(exc)}")

            return None

    @staticmethod
    async def pop_post() -> Post | None:
        try:
            await QueueRepository._ensure_queue_file()

            queue = await QueueRepository._get_queue()

            if queue:
                post = queue.pop(0)

                await QueueRepository._update_queue(queue)

                return post

            return None

        except Exception as exc:
            logger.error(f"{ErrorType.QUEUE_REPOSITORY_ERROR.value}: {str(exc)}")

            return None
