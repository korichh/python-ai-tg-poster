import asyncio

import schedule

from .post import PostJob
from .queue import QueueJob


async def init_jobs() -> None:
    schedule.every().day.at("10:00").do(PostJob.publish_analytics_post)
    schedule.every().day.at("19:00").do(PostJob.publish_news_meme_post)
    schedule.every(5).minutes.do(QueueJob.publish_queue_post)

    while True:
        schedule.run_pending()
        await asyncio.sleep(1)
