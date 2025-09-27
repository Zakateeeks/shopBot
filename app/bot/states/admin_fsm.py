from aiogram import Router, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram.fsm.context import FSMContext

from app.config import settings
from app.services.admin_service import AdminService
from app.bot.keyboards.admin import admin_panel

router = Router()

class AdminAuth(StatesGroup):
    waiting_for_password = State()

@router.message(F.text=="/auth")
async def auth(message: Message, state:FSMContext ,session: AsyncSession):
    service = AdminService(session)
    is_admin = await service.check_admin(message.from_user.username, message.from_user.first_name)
    await message.delete()
    if is_admin is None:
        await message.answer("Введите пароль для входа в админ-панель:")
        await state.set_state(AdminAuth.waiting_for_password)

@router.message(AdminAuth.waiting_for_password)
async def process_admin_password(message: Message, state: FSMContext, session: AsyncSession):
    password = message.text.strip()
    if password == settings.admin_pass:
        service = AdminService(session)
        await service.add_admin(message.from_user.username, message.from_user.first_name)

        await message.answer("Пароль верный! Теперь у вас есть доступ в админ панель.", reply_markup=admin_panel())
        await state.clear()
    else:
        await message.answer("Неверный пароль. Попробуйте снова или введите /start.")
        await state.clear()