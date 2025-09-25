from app.database.operations_product import *
from sqlalchemy.ext.asyncio import AsyncSession


class ProductService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_products(self) -> list[int]:
        return await get_products(self.session)

    async def get_product(self, product_id: int) -> Product | None:
        return await get_product_by_id(self.session, product_id)

    async def get_next_product(self, product_id: int, category: str) -> Product | None:
        return await get_next(self.session, product_id, category)

    async def get_prev_product(self, product_id: int, category: str) -> Product | None:
        return await get_prev(self.session, product_id, category)

    async def get_all_categories(self) -> list[int] | None:
        return await get_categories(self.session)

    async def get_product_on_category(self, category: str) -> Product | None:
        return await get_first_prod_category(self.session, category)

    async def get_basket(self, username: str) -> list | None:
        return await get_product_from_basket(self.session, username)
