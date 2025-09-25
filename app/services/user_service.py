from sqlalchemy.ext.asyncio import AsyncSession
from app.database import operations_user, models

class UserService:
    """
    Сервис для работы с пользователями (business logic).
    """
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_or_create_user(self, tg_id: str, tg_name: str) -> models.User:
        user = await operations_user.get_user_by_tg_id(self.session, tg_id)
        if not user:
            user = await operations_user.create_user(self.session, tg_id, tg_name)
        return user

    async def update_user_contact(self, tg_id: str, contact_name: str, contact_address: str, contact_phone: str):
        return await operations_user.update_user(
            self.session, tg_id,
            contact_name=contact_name,
            contact_address=contact_address,
            contact_phone=contact_phone
        )
    async def add_to_basket(self, tg_id: str, product_id: int, count: int = 1) -> models.User:
        return await operations_user.add_to_basket(self.session, tg_id, product_id=product_id, count=count)