from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String(55)) 
    password = Column(String(55)) 
    
    chats = relationship("Chat", backref="user")
    
    def __repr__(self):
        return  "\n<User "\
        + f"id={self.id}, "\
        + f"username={self.username}, "\
        + f"password={self.password}"\
        ">\n"
       
        