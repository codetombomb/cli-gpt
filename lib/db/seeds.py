from models import (
    User,
    Chat,
    Question,
    Response,
)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///cli-gpt.db")
Session = sessionmaker(bind=engine)
session = Session()

from faker import Faker

fake = Faker()

session.query(User).delete()
session.query(Chat).delete()
session.query(Question).delete()
session.query(Response).delete()

session.commit()


def make_profile():
    first_name = fake.first_name().lower()
    last_name = fake.last_name().lower()
    username = f"{first_name}_{last_name}"
    return {
        "username": username,
        "password": fake.password(length=20),
    }


def seed_users():
    tom =  User(username="tombomb", password="tombomb")
    session.add(tom)
    session.commit()
    
    for _ in range(30):
        profile = make_profile()
        user = User(
            username=profile["username"],
            password=profile["password"],
        )
        session.add(user)
        session.commit()


def seed_chats():
    users = session.query(User).all()
    for user in users:
        for _ in range(5):
            chat = Chat(user_id=user.id, description=fake.paragraph(nb_sentences=2)[0:15] + "...")
            session.add(chat)
            session.commit()
            for _ in range(4):
                question = Question(text=fake.paragraph(nb_sentences=5), chat_id=chat.id)
                response = Response(text=fake.paragraph(nb_sentences=10), chat_id=chat.id)
                session.add(question)
                session.add(response)
                session.commit()

# seed_users()
# seed_chats()

# import ipdb; ipdb.set_trace()