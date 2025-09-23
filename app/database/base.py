from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings

Base = declarative_base()
engine = create_async_engine(settings.database_url, echo=False, future=True)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)