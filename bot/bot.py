from aiogram import Bot

from .utils.env import get_env

BOT_TOKEN = get_env("BOT_TOKEN")

bot = Bot(BOT_TOKEN)
