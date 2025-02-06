import logging
import os

from aiogram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    logging.critical("Missing BOT_TOKEN environment variable.")
    raise SystemExit(1)

bot = Bot(BOT_TOKEN)
