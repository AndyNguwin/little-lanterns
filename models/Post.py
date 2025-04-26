from BaseModel import BaseModel
from User import User
from sqlalchemy import relationship, DateTime, ForeignKey, Mapped, mapped_column

class Post(BaseModel):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True, auto_increment=True)
    title: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), nullable=False)
    creation_time: Mapped[DateTime] = mapped_column(nullable=False)

    user: Mapped[User] = relationship(
        back_populate = "posts"
    )
    def __repr__(self):
        return f"<Post(id={self.id}, title={self.title}, content={self.ontent}, \
            user_id={self.user_id}, creation_time={self.creation_time})>"