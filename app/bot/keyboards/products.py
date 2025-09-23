from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class ProductNav(CallbackData, prefix="product"):
    index: int

def navbar_product():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
    #ToDO
    ])
    return keyboard
