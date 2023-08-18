from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base
from .session import session

class Response(Base):
    __tablename__ = "responses"
    
    id = Column(Integer, primary_key=True)
    text = Column(String) 

    chat_id = Column(Integer, ForeignKey("chats.id"))
    
    @classmethod
    def create(cls,**kwargs):
        new_response = cls(**kwargs)
        new_response.save()
        return new_response
    
    def save(self):
        session.add(self)
        session.commit()
    
    def __repr__(self):
        return "\n<Response "\
            + f"id={self.id}, "\
            + f"text={self.text}, "\
            ">\n"