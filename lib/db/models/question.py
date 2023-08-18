from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base

class Question(Base):
    __tablename__ = "questions"
    
    id = Column(Integer, primary_key=True)
    text = Column(String)
    
    chat_id = Column(Integer, ForeignKey("chat.id"))