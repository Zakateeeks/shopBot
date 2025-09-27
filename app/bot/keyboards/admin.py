from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.bot.keyboards.user import MenuUser


def admin_panel():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text="Добавить товар",
                callback_data=MenuUser(action="add_product", id=0).pack()
            ),
            InlineKeyboardButton(
                text="Редактировать товар",
                callback_data=MenuUser(action="edit_product", id=0).pack()
            )],
            [InlineKeyboardButton(
                text="Список активных заказов",
                callback_data=MenuUser(action="active_orders", id=0).pack()
            )]
        ]

    )
    return keyboard
