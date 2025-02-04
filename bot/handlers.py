from aiogram.types import Message
from sqlalchemy import select, update

from database.db import Session
from database.models import User


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
