from typing import Callable, Awaitable, Dict, Any
from aiogram import BaseMiddleware
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession


class DbSessionMiddleware(BaseMiddleware):
    def __init__(self, session_pool: async_sessionmaker[AsyncSession]):
        super().__init__()
        self.session_pool = session_pool

    async def __call__(
        self,
        handler: Callable[[Any, Dict[str, Any]], Awaitable[Any]],
        event: Any,
        data: Dict[str, Any],
    ) -> Any:
        async with self.session_pool() as session:
            data["session"] = session
            return await handler(event, data)