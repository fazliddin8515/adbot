from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from sqlalchemy import select, update

from bot.bot import bot
from database.db import Session
from database.models import User
from utils.env import get_env

from .keyboards import yes_no_keyboard

ROOT_ID = get_env("ROOT_ID")


async def start_handler(msg: Message) -> None:
    from_user = msg.from_user
    if from_user is not None:
        with Session() as session:
            select_stmt = select(User).where(User.id == from_user.id)
            result = session.execute(select_stmt)
            if result.scalar_one_or_none() is None:
                user = User(
                    id=from_user.id,
                    is_bot=from_user.is_bot,
                    first_name=from_user.first_name,
                    last_name=from_user.last_name,
                    username=from_user.username,
                    language_code=from_user.language_code,
                )
                session.add(user)
                session.commit()
                await msg.answer(f"{from_user.first_name} is registred")
            else:
                update_stmt = (
                    update(User)
                    .where(User.id == from_user.id)
                    .values(
                        first_name=from_user.first_name,
                        last_name=from_user.last_name,
                        username=from_user.username,
                        language_code=from_user.language_code,
                    )
                )
                session.execute(update_stmt)
                session.commit()
                await msg.answer(f"{from_user.first_name} is updated")


async def add_admin_handler(msg: Message) -> None:
    from_user = msg.from_user
    if (
        (from_user is not None)
        and (msg.text is not None)
        and (from_user.id == int(ROOT_ID))
    ):
        with Session() as session:
            username = msg.text.split(" ")[1].strip()
            if username[0] == "@":
                select_stmt = select(User).where(User.username == username[1:])
                existing_user = session.scalars(select_stmt).first()
                if existing_user is not None:
                    if not existing_user.is_admin:
                        existing_user.is_admin = True
                        session.commit()
                        await msg.answer(f"The {username} is added to the admins list")
                    else:
                        await msg.answer(
                            f"The {username} is already added to the admins list"
                        )
                else:
                    await msg.answer(f"The {username} user hasn't started the bot yet")
            else:
                await msg.answer(
                    f"The {username} username must begin with the '@' symbol"
                )


async def remove_admin_handler(msg: Message) -> None:
    from_user = msg.from_user
    if (
        (from_user is not None)
        and (msg.text is not None)
        and (from_user.id == int(ROOT_ID))
    ):
        with Session() as session:
            username = msg.text.split(" ")[1].strip()
            if username[0] == "@":
                select_stmt = select(User).where(User.username == username[1:])
                existing_user = session.scalars(select_stmt).first()
                if existing_user is not None:
                    if existing_user.is_admin:
                        existing_user.is_admin = False
                        session.commit()
                        await msg.answer(
                            f"The {username} is removed to the admins list"
                        )
                    else:
                        await msg.answer(f"The {username} isn't on the admins list")


async def post_handler(msg: Message, state: FSMContext) -> None:
    from_user = msg.from_user
    if (from_user is not None) and (msg.md_text is not None):
        post = msg.md_text[5:].strip()
        if len(post) != 0:
            await state.update_data(post=post)
            await msg.answer("Do you want to send the post?")
            await msg.answer(
                post,
                parse_mode=ParseMode.MARKDOWN_V2,
                reply_markup=yes_no_keyboard,
            )
        else:
            await msg.answer("post is empty")


async def send_post_handler(cb: CallbackQuery, state: FSMContext) -> None:
    if isinstance(cb.message, Message):
        from_user = cb.message.chat
        data = await state.get_data()
        post = data.get("post")
        with Session() as session:
            select_stmt = select(User)
            users = session.scalars(select_stmt).all()
            select_stmt = select(User).where(User.is_admin)
            admins = session.scalars(select_stmt).all()
            admin_ids = {admin.id for admin in admins}

        if (from_user.id == int(ROOT_ID)) or (from_user.id in admin_ids):
            for user in users:
                await bot.send_message(user.id, post, parse_mode=ParseMode.MARKDOWN_V2)
            await cb.message.edit_reply_markup(reply_markup=None)
            await cb.message.reply("Post is sent")
        else:
            await cb.message.edit_reply_markup(reply_markup=None)
            await cb.message.reply("You don't have permissions for sending posts")


async def cancel_post_handler(cb: CallbackQuery) -> None:
    if isinstance(cb.message, Message):
        await cb.message.edit_reply_markup(reply_markup=None)
        await cb.message.reply("Post is canceled")
