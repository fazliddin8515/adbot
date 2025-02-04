from aiogram.types import Message
from sqlalchemy import select, update

from database.db import Session
from database.models import User
from utils.env import get_env

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
                        await msg.answer(f"The {username} added to the admins list")
                    else:
                        await msg.answer(
                            f"The {username} already added to the admins list"
                        )
                else:
                    await msg.answer(f"The {username} user hasn't started the bot")
            else:
                await msg.answer(
                    f"The {username} username must begin with the '@' symbol"
                )
