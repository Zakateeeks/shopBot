from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database.models import Product

async def get_products(session: AsyncSession) -> list[int]:
    result = await session.execute(
        select(Product.id).order_by(Product.id)
    )
    return [row[0] for row in result.all()]

async def get_product_by_id(session: AsyncSession, product_id: int) -> Product:
    result = await session.execute(select(Product.id).where(Product.id == product_id))
    return result.scalar_one_or_none()

