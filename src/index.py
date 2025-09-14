import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from commands import init_commands
from constants import ENV
from jobs import init_jobs
from local_types import ErrorType
from utils import logger


async def main():
    try:
        bot = Bot(token=ENV["telegram_bot_token"])
        storage = MemoryStorage()
        dp = Dispatcher(storage=storage)

        init_commands(dp)
        asyncio.create_task(init_jobs(bot))

        logger.info("Bot started")
        await dp.start_polling(bot)

    except Exception as exc:
        logger.error(f"{ErrorType.MAIN_ERROR.value}: {str(exc)}")

    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
