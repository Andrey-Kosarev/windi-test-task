from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, UUID, func

from src.persistence.postgres.connection.metadata import Base


class Messages(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, autoincrement=True)
    idempotency_key = Column(UUID, nullable=False, unique=True)
    chat_id = Column(Integer, ForeignKey("chats.id"), nullable=False)
    sender_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    text = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False, server_default=func.now())
    is_read = Column(Boolean, nullable=False, server_default="False")
