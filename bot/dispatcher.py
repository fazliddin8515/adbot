from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage

from .handlers import (
    add_admin_handler,
    cancel_post_handler,
    post_handler,
    remove_admin_handler,
    send_post_handler,
    start_handler,
)

dp = Dispatcher(storage=MemoryStorage())

dp.message.register(start_handler, Command("start"))
dp.message.register(add_admin_handler, Command("add_admin"))
dp.message.register(remove_admin_handler, Command("remove_admin"))
dp.message.register(post_handler, Command("post"))

dp.callback_query.register(send_post_handler, lambda c: c.data == "send_post")
dp.callback_query.register(cancel_post_handler, lambda c: c.data == "cancel_post")
