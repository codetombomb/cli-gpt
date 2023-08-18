from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base

class Response(Base):
    __tablename__ = "responses"
    
    id = Column(Integer, primary_key=True)
    text = Column(String) 

    chat_id = Column(Integer, ForeignKey("chats.id"))
    
    def __repr__(self):
        return "\n<Response "\
            + f"id={self.id}, "\
            + f"text={self.text}, "\
            ">\n"