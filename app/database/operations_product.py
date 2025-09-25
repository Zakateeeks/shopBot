from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database.models import User
from app.database.models import Product

async def get_products(session: AsyncSession) -> list[int]:
    result = await session.execute(
        select(Product.id).order_by(Product.id)
    )
    return [row[0] for row in result.all()]

async def get_product_by_id(session: AsyncSession, product_id: int) -> Product:
    result = await session.execute(select(Product).where(Product.id == product_id))
    return result.scalar_one_or_none()

async def get_next(session: AsyncSession, product_id: int, category: str) -> Product:
    result = await session.execute(
        select(Product)
        .where((Product.id > product_id) & (Product.category == category))
        .order_by(Product.id.asc())
        .limit(1)
    )
    return result.scalar_one_or_none()

async def get_prev(session: AsyncSession, product_id: int, category: str) -> Product:
    result = await session.execute(
        select(Product)
        .where((Product.id < product_id) & (Product.category == category))
        .order_by(Product.id.desc())
        .limit(1)
    )
    return result.scalar_one_or_none()

async def get_categories(session: AsyncSession) -> list[str] | None:
    result = await session.execute(
        select(Product.category).order_by(Product.category.asc())
    )
    return [row[0] for row in result.all()]

async def get_first_prod_category(session: AsyncSession, category: str) -> Product:
    result = await session.execute(
        select(Product)
        .where(Product.category == category)
        .order_by(Product.id.asc())
        .limit(1)
    )

    return result.scalar_one_or_none()

async def get_product_from_basket(session: AsyncSession, username: str) -> list | None:
    result = await session.execute(
        select(User.basket)
        .where (User.tg_id == username)
    )
    return [row[0] for row in result.all()]

async def remove_product_from_basket(session: AsyncSession, username: str, product_id: int) -> User | None:
    result = await session.execute(
        select(User)
        .where (User.tg_id == username)
    )
    user= result.scalars().first()

    basket = user.basket
    new_basket = []
    for item in basket:
        if item["id"] != product_id:
            new_basket.append(item)

    user.basket = new_basket
    await session.commit()
    await session.refresh(user)