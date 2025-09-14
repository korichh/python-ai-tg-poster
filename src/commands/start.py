from aiogram import Router, types
from aiogram.filters import Command

from local_types import ErrorType
from utils import logger

router = Router()


@router.message(Command("start"))
async def start_command(message: types.Message):
    try:
        await message.answer(
            "Hello! Please use the /post command to create a new post."
        )

    except Exception as exc:
        await message.answer("An unexpected error occured. Please check the logs.")
        logger.error(f"{ErrorType.START_COMMAND_ERROR}: {str(exc)}")
