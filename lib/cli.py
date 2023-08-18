from db.models import User, Chat, Question, Response

class Cli():
    
    def start():
        user_question = input("Send a message:\n")
        