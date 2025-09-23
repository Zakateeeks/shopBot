from app.database.models import Product
from app.database.operations_product import get_product_by_id, get_products
from sqlalchemy.ext.asyncio import AsyncSession


class ProductService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_products(self) -> list[int]:
        return await get_products(self.session)

    async def get_product(self, product_id: int) -> Product | None:
        return await get_product_by_id(self.session, product_id)
