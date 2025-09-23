from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from app.bot.keyboards.user import MenuUser, back_to_profile
from app.services.user_service import UserService

router = Router()

class ProfileForm(StatesGroup):
    waiting_for_name = State()
    waiting_for_phone = State()
    waiting_for_address = State()

@router.callback_query(MenuUser.filter(F.action == "edit_profile"))
async def edit_profile(callback: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(ProfileForm.waiting_for_name)
    sent_msg = await callback.message.edit_text("Введите ваше ФИО:")
    await state.update_data(bot_msg_id=sent_msg.message_id)
    await callback.answer()

@router.message(ProfileForm.waiting_for_name)
async def edit_name(message: Message, state: FSMContext) -> None:
    await state.update_data(contact_name=message.text)
    await state.set_state(ProfileForm.waiting_for_phone)
    await message.delete()
    data = await state.get_data()
    bot_msg_id = data.get("bot_msg_id")

    await message.bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=bot_msg_id,
        text="Введите телефон для связи:"
    )

@router.message(ProfileForm.waiting_for_phone)
async def edit_phone(message: Message, state: FSMContext) -> None:
    await state.update_data(contact_phone=message.text)
    await state.set_state(ProfileForm.waiting_for_address)
    data = await state.get_data()
    bot_msg_id = data.get("bot_msg_id")

    await message.bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=bot_msg_id,
        text="Введите адрес доставки:"
    )

    await message.delete()

@router.message(ProfileForm.waiting_for_address)
async def edit_address(message: Message, state: FSMContext, session: AsyncSession) -> None:
    await state.update_data(contact_address=message.text)
    data = await state.get_data()
    await message.delete()

    service = UserService(session)
    await service.update_user_contact(
        tg_id=str(message.from_user.username),
        contact_name=data["contact_name"],
        contact_phone=data["contact_phone"],
        contact_address=data["contact_address"],
    )
    user = await service.get_or_create_user(message.from_user.username,
                                            message.from_user.first_name)

    text = (f"✅ Профиль обновлён!\n\n"
            f"ФИО: {user.contact_name}\n"
            f"Телефон: {user.contact_phone}\n"
            f"Адрес доставки: {user.contact_address}")
    data = await state.get_data()
    bot_msg_id = data.get("bot_msg_id")

    await message.bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=bot_msg_id,
        text=text,
        reply_markup=back_to_profile()
    )
    await state.clear()