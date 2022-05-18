from .base import Base
from sqlalchemy import Column, Integer, String


class Media_Type(Base):
    __tablename__ = "media_type"

    id = Column(Integer)
    name = Column(String)