from typing import List
from models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import DateTime
from datetime import datetime
from sqlalchemy import func
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models import Post

class User(BaseModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    creation_time: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=func.now())

    posts: Mapped[List["Post"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, first_name={self.first_name}, last_name={self.last_name})>"
