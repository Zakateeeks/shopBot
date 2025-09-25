from aiogram import Router, F
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from app.bot.keyboards.products import view_categories, navbar_product
from app.bot.keyboards.user import MenuUser
from app.services.product_service import ProductService
from app.services.user_service import UserService

router = Router()

@router.callback_query(MenuUser.filter(F.action == "catalog"))
async def choice_category(callback: CallbackQuery, session: AsyncSession):
    service = ProductService(session)
    categories = await service.get_all_categories()

    await callback.message.edit_text("Товары какой категории вы хотите посмотреть?", reply_markup=view_categories(categories))

@router.callback_query(MenuUser.filter(F.action == "view_prod"))
async def view_catalog(callback: CallbackQuery,callback_data: MenuUser, session: AsyncSession):
    service = ProductService(session)
    category = callback_data.temp_data
    if not callback_data.id:
        product = await service.get_product_on_category(category)
    else:
        product = await service.get_product(callback_data.index)

    if not product:
        await callback.answer("Нет товаров в этой категории", show_alert=True)
        return

    prev_product = await service.get_prev_product(product_id=product.id,
                                                  category=category)
    next_product = await service.get_next_product(product_id=product.id,
                                                  category=category)
    prev_id = prev_product.id if prev_product else None
    next_id = next_product.id if next_product else None

    keyboard = navbar_product(product.id, prev_id, next_id, category)

    await callback.message.edit_text(
        text=f"Товар: {product.name}\nЦена: {product.price}",
        reply_markup=keyboard
    )
    await callback.answer()

@router.callback_query(MenuUser.filter(F.action == "add_to_basket"))
async def add_to_basket(callback: CallbackQuery, callback_data: MenuUser, session: AsyncSession):
    service_user = UserService(session)
    service_product = ProductService(session)
    product = await service_product.get_product(callback_data.index)
    await callback.answer(text=f"{product.name} помещен в корзину", show_alert=True)
    await service_user.add_to_basket(callback.from_user.username, product.id, 1)

@router.callback_query(MenuUser.filter(F.action == "basket"))
async def get_basket(callback: CallbackQuery, callback_data: MenuUser, session: AsyncSession):
    service_user = UserService(session)
    service_product = ProductService(session)
    basket = (await service_product.get_basket(callback.from_user.username))[0]
    product_ids = [row["id"] for row in basket]
    this_id = callback_data.id

    prev_id = None if this_id != 0 else product_ids[this_id - 1]
    next_id = None if this_id != len(product_ids)-1 else product_ids[this_id + 1]

    keyboard = navbar_product(product_ids[this_id], prev_id, next_id) #ToDo
    #Переписать под навбар корзины
