import asyncio
import signal

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from commands import init_commands
from constants import ENV
from jobs import init_jobs
from local_types import ErrorType
from utils import logger, stop_app


async def main():
    try:
        signal.signal(signal.SIGINT, stop_app)
        signal.signal(signal.SIGTERM, stop_app)

        bot = Bot(token=ENV["TELEGRAM_BOT_TOKEN"])
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
