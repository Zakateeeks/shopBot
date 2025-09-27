from sqlalchemy.ext.asyncio import AsyncSession
from app.database import models, operations_admin


class AdminService:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def check_admin(self, tg_id: str, tg_name: str) -> models.User:
        return await operations_admin.check_user_is_admin(self.session, tg_id, tg_name)

    async def add_admin(self, tg_id: str, tg_name: str) -> models.User:
        return await operations_admin.set_user_is_admin(self.session, tg_id, tg_name)