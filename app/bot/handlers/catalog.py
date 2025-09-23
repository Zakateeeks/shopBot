import logging
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.product_service import ProductService
from app.bot.keyboards.user import start_menu, profile_menu, MenuUser

logger = logging.getLogger(__name__)
router = Router()


@router.callback_query(MenuUser.filter(F.action=="catalog"))
async def view_catalog(callback_query: CallbackQuery, session: AsyncSession):
    service = ProductService(session)
    product = await service.get_product()

