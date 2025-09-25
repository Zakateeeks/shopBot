from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData

class MenuUser(CallbackData, prefix="menu"):
    action: str = ""
    id: int = 0
    temp_data: str = ""
    index: int = 0

def start_menu():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="👤 Профиль",
                    callback_data=MenuUser(action="profile", id=0).pack()
                )
            ],
            [
                InlineKeyboardButton(
                    text="🛍 Мои заказы",
                    callback_data=MenuUser(action="orders", id=0).pack()
                ),
                InlineKeyboardButton(
                    text="🛒 Корзина",
                    callback_data=MenuUser(action="basket", id=0).pack()
                )
            ],
            [
                InlineKeyboardButton(
                    text="📗 Каталог",
                    callback_data=MenuUser(action="catalog", id=0).pack()
                )
            ]
        ]
    )
    return keyboard

def profile_menu():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text="📝 Редактировать",
                callback_data=MenuUser(action="edit_profile", id=0).pack()
            )],
            [InlineKeyboardButton(
                text="🛒 Корзина",
                callback_data=MenuUser(action="basket", id=0).pack()
            ),
            InlineKeyboardButton(
                text="🛍 Мои заказы",
                callback_data=MenuUser(action="orders", id=0).pack()
            )],
            [
                InlineKeyboardButton(
                    text="📗 Каталог",
                    callback_data=MenuUser(action="catalog", id=0).pack()
                )
            ]
        ]
    )

    return keyboard

def back_to_profile():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text="👤 Профиль",
                callback_data=MenuUser(action="profile", id=0).pack()
            )]
        ]
    )
    return keyboard
