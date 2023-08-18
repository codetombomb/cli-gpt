from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Chat(Base):
    __tablename__ = "chats"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    questions = relationship("Question", backref="chat")
    responses = relationship("Response", backref="chat")
    
    
    def __repr__(self):
        return "\n<Chat "\
            + f"id={self.id}, "\
            + f"user_id={self.user_id}, "\
            ">\n"
                