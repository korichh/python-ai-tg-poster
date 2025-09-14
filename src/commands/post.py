from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from local_types import ErrorType
from repositories import QueueRepository
from utils import logger


class PostStates(StatesGroup):
    waiting_for_post = State()


router = Router()


@router.message(Command("post"))
async def post_command(message: types.Message, state: FSMContext):
    try:
        await message.answer("Please send your post, and I will add it to the queue.")
        await state.set_state(PostStates.waiting_for_post)

    except Exception as exc:
        await message.answer("An unexpected error occured. Please check the logs.")
        logger.error(f"{ErrorType.POST_COMMAND_ERROR}: {str(exc)}")


@router.message(F.text | F.photo, PostStates.waiting_for_post)
async def receive_post(message: types.Message, state: FSMContext):
    try:
        photo = message.photo[-1] if message.photo else None
        text = message.caption or message.text

        if not text:
            await message.answer(
                "Your post must contain text and an optional image. Please try again."
            )

            return

        QueueRepository.add_post(text, photo.file_id)

        logger.info("New post added to the queue")

        await message.answer(
            "Your post has been successfully added to the queue and will be published within 5 minutes."
        )

        await state.clear()

    except Exception as exc:
        await message.answer("An unexpected error occured. Please check the logs.")
        logger.error(f"{ErrorType.POST_MESSAGE_ERROR}: {str(exc)}")
