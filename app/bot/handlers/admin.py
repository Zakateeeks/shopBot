from aiogram.types import Message
from aiogram import Router, F
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.user_service import UserService
from app.bot.keyboards.admin import *

router = Router()

@router.message(F.text == "/admin")
async def admin_handler(message: Message, session: AsyncSession):
    service = UserService(session)
    user = await service.get_or_create_user(message.from_user.username, message.from_user.first_name)

    #ToDo реализовать проверку на админа

    await message.answer(text=f"Приветствуем вас в нашем магазине,"
                         f" {user.tg_name}!", reply_markup=())
