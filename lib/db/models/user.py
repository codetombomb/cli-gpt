from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .session import session
from .base import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String(55), unique=True) 
    password = Column(String(55)) 
    
    chats = relationship("Chat", backref="user")
    
    @classmethod
    def create(cls, **kwargs):
        user = User(**kwargs)
        session.add(user)
        session.commit()
        return user

    @classmethod
    def find_by(cls, **kwargs):
        found_user = session.query(cls).filter_by(**kwargs).first()
        if found_user:
            return found_user
        
    
    def __repr__(self):
        return  "\n<User "\
        + f"id={self.id}, "\
        + f"username={self.username}, "\
        + f"password={self.password}"\
        ">"
       
        