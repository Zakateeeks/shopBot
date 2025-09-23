import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import ErrorEvent
from app.database.base import async_session_maker
from app.bot.middleware.db import DbSessionMiddleware
from app.config import settings
from app.database.base import Base, engine
from app.bot.routers import main_router
async def main():
    logger = logging.getLogger(__name__)

    bot = Bot(settings.bot_token)
    dp = Dispatcher()
    dp.update.middleware(DbSessionMiddleware(async_session_maker))
    dp.include_router(main_router)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    @dp.errors()
    async def error_handler(event: ErrorEvent):
        logger.error("Ошибка: %s", event.exception, exc_info=True)
    logger.info("Старт бота...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())