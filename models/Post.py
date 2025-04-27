from models import BaseModel
from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models import User

class Post(BaseModel):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), nullable=False)
    creation_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    user: Mapped["User"] = relationship(
        back_populates = "posts"
    )
    def __repr__(self):
        return f"<Post(id={self.id}, title={self.title}, content={self.ontent}, \
            user_id={self.user_id}, creation_time={self.creation_time})>"