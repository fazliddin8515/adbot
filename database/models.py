from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    is_bot: Mapped[bool] = mapped_column(default=False)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=True)
    username: Mapped[str] = mapped_column(nullable=True, unique=True)
    language_code: Mapped[str] = mapped_column(String(2), nullable=True)
    is_admin: Mapped[bool] = mapped_column(default=False)
