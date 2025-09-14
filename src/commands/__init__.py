from .post import router as post_router
from .start import router as start_router


def init_commands(dp) -> None:
    dp.include_router(start_router)
    dp.include_router(post_router)
