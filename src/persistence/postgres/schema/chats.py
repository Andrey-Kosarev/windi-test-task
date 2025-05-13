from sqlalchemy import Column, String, Integer
from src.persistence.postgres.connection.metadata import Base

class Chats(Base):
    __tablename__ = 'chats'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)


