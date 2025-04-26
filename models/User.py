from typing import List
from BaseModel import BaseModel
from Post import Post
from sqlalchemy.orm import Mapped, mapped_column, DateTime, relationship

class User(BaseModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    creation_time: Mapped[DateTime] = mapped_column(nullable=False)

    posts: Mapped[List["Post"]] = relationship(
        backpopulates="users", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, first_name={self.first_name}, last_name={self.last_name})>"
