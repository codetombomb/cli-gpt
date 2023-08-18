from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///db/cli-gpt.db")
Session = sessionmaker(bind=engine)
session = Session() 