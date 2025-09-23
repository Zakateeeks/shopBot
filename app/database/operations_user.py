from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database.models import User

async def get_user_by_tg_id(session: AsyncSession, tg_id: str) -> User | None:
    result = await session.execute(select(User).where(User.tg_id == tg_id))
    return result.scalar_one_or_none()

async def create_user(session: AsyncSession, tg_id: str, tg_name: str) -> User:
    user = User(tg_id=tg_id, tg_name=tg_name)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user

async def update_user(session: AsyncSession,tg_id: str, contact_name: str, contact_address: str, contact_phone: str) -> User | None:
    result = await session.execute(select(User).where(User.tg_id == tg_id))
    user = result.scalar_one_or_none()

    user.contact_name = contact_name
    user.contact_address = contact_address
    user.contact_phone = contact_phone

    await session.commit()
    await session.refresh(user)

