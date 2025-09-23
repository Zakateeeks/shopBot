from aiogram import Router
import app.bot.handlers.user as user_handler
import app.bot.states.user_fsm as states

main_router = Router()
main_router.include_router(user_handler.router)
main_router.include_router(states.router)