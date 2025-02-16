import asyncio
import logging
import os
from pathlib import Path

from bot.bot import bot, commands, set_bot_commands
from bot.dispatcher import dp

Path("logs").mkdir(exist_ok=True)

log_level = os.getenv("LOG_LEVEL", "INFO").upper()

logging.basicConfig(
    level=getattr(logging, log_level, logging.INFO),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(Path("logs") / "aiogram.log"),
    ],
)


async def on_start() -> None:
    await set_bot_commands(commands)


async def on_shutdown() -> None:
    logging.info("Bot is shutting down...")
    await bot.session.close()


async def main() -> None:
    try:
        dp.startup.register(on_start)
        dp.shutdown.register(on_shutdown)
        await dp.start_polling(bot)
    except asyncio.CancelledError:
        logging.info("Polling was cancelled. Shutting down gracefully...")
    except TimeoutError as e:
        logging.error("Timeout error: %s", e, exc_info=True)
    except Exception as e:
        logging.error("Bot encountered an error: %s", e, exc_info=True)


if __name__ == "__main__":
    asyncio.run(main())
