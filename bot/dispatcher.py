from aiogram import Dispatcher
from aiogram.filters import Command

from .handlers import start_handler

dp = Dispatcher()

dp.message.register(start_handler, Command("start"))
