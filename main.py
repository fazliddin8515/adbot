import asyncio

from aiogram import Bot

from .bot.bot import bot
from .bot.dispatcher import dp


async def on_start(bot: Bot) -> None:
    bot_info = await bot.get_me()
    print(f"https://t.me/{bot_info.username} has been started...")


async def main() -> None:
    dp.startup.register(on_start)
    await dp.start_polling(bot)


asyncio.run(main())
