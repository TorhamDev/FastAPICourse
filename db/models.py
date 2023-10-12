from sqlalchemy.orm import Mapped, mapped_column

from .engine import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str | None] = mapped_column(
        unique=True, default=None, nullable=True
    )
    password: Mapped[str] = mapped_column()
