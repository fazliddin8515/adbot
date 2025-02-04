from aiogram import Dispatcher
from aiogram.filters import Command

from .handlers import add_admin_handler, start_handler

dp = Dispatcher()

dp.message.register(start_handler, Command("start"))
dp.message.register(add_admin_handler, Command("add_admin"))
