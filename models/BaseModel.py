from sqlalchemy.orm import DeclarativeBase

class BaseModel(DeclarativeBase):
    __abstract__ = True

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.__dict__}>"