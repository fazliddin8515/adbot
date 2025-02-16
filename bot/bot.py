import logging
import os

from aiogram import Bot
from aiogram.types.bot_command import BotCommand

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    logging.error("Missing BOT_TOKEN environment variable.")
    raise SystemExit(1)

bot = Bot(BOT_TOKEN)

commands: list[BotCommand] = [
    BotCommand(command="start", description="register user"),
    BotCommand(command="post", description="send post"),
    BotCommand(command="add_admin", description="add admin"),
    BotCommand(command="remove_admin", description="remove admin"),
]


async def set_bot_commands(commands: list[BotCommand]) -> None:
    await bot.set_my_commands(commands)
