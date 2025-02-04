from datetime import datetime

from sqlalchemy import String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    is_bot: Mapped[bool] = mapped_column(default=False, nullable=False)
    first_name: Mapped[str] = mapped_column(String(55), nullable=False)
    last_name: Mapped[str] = mapped_column(String(55), nullable=True)
    username: Mapped[str] = mapped_column(String(55), unique=True, nullable=True)
    language_code: Mapped[str] = mapped_column(String(2), nullable=True)
    is_admin: Mapped[bool] = mapped_column(default=False, nullable=False)

    created_at: Mapped[datetime] = mapped_column(default=func.now(), nullable=False)
    updated_ad: Mapped[datetime] = mapped_column(
        default=func.now(), onupdate=func.now(), nullable=False
    )

    def __repr__(self) -> str:
        return f"<User(id={self.id}, firt_name={self.first_name}), username={self.username}>"  # noqa: E501
