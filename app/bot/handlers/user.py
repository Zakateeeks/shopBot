import logging
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.user_service import UserService
from app.bot.keyboards.user import start_menu, profile_menu, MenuUser

logger = logging.getLogger(__name__)
router = Router()

@router.message(F.text == "/start")
async def start_handler(message: Message, session: AsyncSession):
    service = UserService(session)
    user = await service.get_or_create_user(message.from_user.username, message.from_user.first_name)
    logger.info(user.tg_name, user.tg_id)

    await message.answer(text=f"Приветствуем вас в нашем магазине,"
                         f" {user.tg_name}!", reply_markup=start_menu())


@router.callback_query(MenuUser.filter(F.action == "profile"))
async def view_profile(callback: CallbackQuery, session: AsyncSession):
    service = UserService(session)
    user = await service.get_or_create_user(callback.from_user.username,
                                            callback.from_user.first_name)
    contact_name = user.contact_name
    contact_phone = user.contact_phone
    contact_adress = user.contact_address
    text = (f"{user.tg_name}, приветствуем тебя в профиле! Вот что мы о тебе знаем:\n"
            f"ФИО для связи: {contact_name if contact_name else "Не знаем(" }\n"
            f"Телефон для связи: {contact_phone if contact_phone else "Не указан"}\n"
            f"Адрес доставки: {contact_adress if contact_adress else "Не указан"}\n")
    await callback.message.edit_text(text=text, reply_markup=profile_menu())
    await callback.answer()

