from aiogram.types import Message
from aiogram import Router, F
from sqlalchemy.ext.asyncio import AsyncSession
from app.bot.keyboards.user import start_menu
from app.bot.keyboards.admin import admin_panel
from app.services.admin_service import AdminService

router = Router()


@router.message(F.text == "/admin")
async def admin_handler(message: Message, session: AsyncSession):
    service = AdminService(session)
    is_admin = await service.check_admin(message.from_user.username, message.from_user.first_name)

    if is_admin:
        await message.answer("Добро пожаловать в админ панель!", reply_markup=admin_panel())
    else:
        await message.answer("Вы не являетесь админом :(",
                                         reply_markup=start_menu())

