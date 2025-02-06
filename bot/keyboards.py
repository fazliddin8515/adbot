from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

yes_no_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Yes", callback_data="send_post"),
            InlineKeyboardButton(text="No", callback_data="cancel_post"),
        ],
    ]
)
