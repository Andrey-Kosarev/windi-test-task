from sqlalchemy import Column, String, Integer, ForeignKey
from src.persistence.postgres.connection.metadata import Base

class Chats(Base):
    __tablename__ = 'chats'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)



class ChatParticipant(Base):
    __tablename__ = "chat_participant"

    id = Column(Integer, primary_key=True, autoincrement=True)
    group_id = Column(Integer, ForeignKey("groups.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

