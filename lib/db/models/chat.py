from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from .base import Base
from .session import session

class Chat(Base):
    __tablename__ = "chats"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    description = Column(String)
    
    questions = relationship("Question", backref="chat")
    responses = relationship("Response", backref="chat")
    
    @classmethod
    def create(cls,**kwargs):
        new_chat = cls(**kwargs)
        new_chat.save()
        return new_chat
    
    @classmethod
    def all_descriptions_for(cls, user_id):
        return ["💬 " + str(desc[0])for desc in session.query(cls.description).filter(cls.user_id == user_id).all()]
    
    @classmethod
    def find_by(cls, **kwargs):
        return session.query(cls).filter_by(**kwargs).first()
    
    def save(self):
        session.add(self)
        session.commit()
    
        
    
    def __repr__(self):
        return "\n<Chat "\
            + f"id={self.id}, "\
            + f"user_id={self.user_id}, "\
            ">\n"
                