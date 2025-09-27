from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database.models import User
async def check_user_is_admin(session: AsyncSession, tg_id: str, tg_name: str) -> User | None:
    result = await session.execute(select(User).where((User.tg_id == tg_id) & (User.tg_name == tg_name)))
    user = result.scalar_one_or_none()
    if user.is_admin is None:
        return None
    else:
        return user

async def set_user_is_admin(session: AsyncSession, tg_id: str, tg_name: str) -> User | None:
    result = await session.execute(select(User).where((User.tg_id == tg_id) & (User.tg_name == tg_name)))
    user = result.scalar_one_or_none()
    user.is_admin = True
    await session.commit()
    await session.refresh(user)