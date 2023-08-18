from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from .session import session

class Chat(Base):
    __tablename__ = "chats"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    questions = relationship("Question", backref="chat")
    responses = relationship("Response", backref="chat")
    
    @classmethod
    def create(cls,**kwargs):
        new_chat = cls(**kwargs)
        new_chat.save()
        return new_chat
    
    def save(self):
        session.add(self)
        session.commit()
    
    def __repr__(self):
        return "\n<Chat "\
            + f"id={self.id}, "\
            + f"user_id={self.user_id}, "\
            ">\n"
                