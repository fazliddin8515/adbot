import asyncio
import logging
import os

from bot.bot import bot
from bot.dispatcher import dp

os.makedirs("logs", exist_ok=True)

log_level = os.getenv("LOG_LEVEL", "INFO").upper()

logging.basicConfig(
    level=getattr(logging, log_level, logging.INFO),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler(), logging.FileHandler("logs/aiogram.log")],
)


async def main() -> None:
    try:
        await dp.start_polling(bot)
    except asyncio.CancelledError:
        logging.info("Polling was cancelled. Shutting down gracefully...")
    except ConnectionError as e:
        logging.error("Timeout error: %s", e, exc_info=True)
    except TimeoutError as e:
        logging.error("Timeout error: %s", e, exc_info=True)
    except Exception as e:
        logging.error("Bot encountered an error: %s", e, exc_info=True)
    finally:
        await bot.session.close()
        logging.info("Bot session closed.")


if __name__ == "__main__":
    asyncio.run(main())
