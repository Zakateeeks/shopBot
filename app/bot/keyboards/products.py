from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.bot.keyboards.user import MenuUser

def navbar_product(curr_id: int,prev_id: int|None, next_id: int|None, category: str) -> InlineKeyboardMarkup:
    keyboard = []
    buttons = []
    if prev_id:
        buttons.append(
            InlineKeyboardButton(
                text="⬅️ Назад",
                callback_data=MenuUser(index=prev_id, action="view_prod", temp_data=category, id=1).pack()
            )
        )
    if next_id:
        buttons.append(
            InlineKeyboardButton(
                text="Вперёд ➡️",
                callback_data=MenuUser(index=next_id, action="view_prod", temp_data=category, id=1).pack()
            )
        )
    keyboard.append(buttons)

    keyboard.append([
        InlineKeyboardButton(
            text="🛒 В корзину",
            callback_data=MenuUser(action="add_to_basket", id=curr_id,
                                   index=curr_id, temp_data=category).pack()
        )
    ])
    keyboard.append([
        InlineKeyboardButton(text="👤 Профиль", callback_data=MenuUser(action="profile", id=0).pack()),
        InlineKeyboardButton(text="🛍 Корзина", callback_data=MenuUser(action="basket", id=0).pack()),
        InlineKeyboardButton(text="🏠 Главная", callback_data=MenuUser(action="main", id=0).pack())
    ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def view_categories(categories: list) -> InlineKeyboardMarkup | None:
    keyboard = []
    for category in set(categories):
        keyboard.append([
            InlineKeyboardButton(text=category, callback_data=MenuUser(action="view_prod", id=0, temp_data=category).pack())
        ])
    keyboard.append([InlineKeyboardButton(text='⬅️ Назад', callback_data=MenuUser(action='main', id=0).pack())])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)
