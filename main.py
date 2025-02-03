import asyncio
import logging
import os

from bot.bot import bot
from bot.dispatcher import dp

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler(), logging.FileHandler("logs/aiogram.log")],
)


async def main() -> None:
    await dp.start_polling(bot)


asyncio.run(main())
