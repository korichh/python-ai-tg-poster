import asyncio

import schedule
from aiogram import Bot

from .post import PostJob
from .queue import QueueJob


def arun(afunc, **kwargs):
    def wrapper():
        asyncio.create_task(afunc(**kwargs))

    return wrapper


async def init_jobs(bot: Bot) -> None:
    schedule.every().day.at("10:00").do(arun(PostJob.publish_analytics_post, bot=bot))
    schedule.every().day.at("19:00").do(arun(PostJob.publish_news_meme_post, bot=bot))
    schedule.every(5).minutes.do(arun(QueueJob.publish_queue_post, bot=bot))

    while True:
        schedule.run_pending()
        await asyncio.sleep(1)
