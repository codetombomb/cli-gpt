from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base
from .session import session

class Question(Base):
    __tablename__ = "questions"
    
    id = Column(Integer, primary_key=True)
    text = Column(String)
    
    chat_id = Column(Integer, ForeignKey("chats.id"))
    
    @classmethod
    def create(cls,**kwargs):
        new_question = cls(**kwargs)
        new_question.save()
        return new_question
    
    def save(self):
        session.add(self)
        session.commit()
        
    def __repr__(self):
        return "\n<Question "\
            + f"id={self.id}, "\
            + f"text={self.text}, "\
            ">\n"