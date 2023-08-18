from db.models import User, Chat, Question, Response
from controller import Controller
from banners import Banner
from prompt import Prompt
from prettycli import yellow, red, color
import time

controller = Controller()
banners = Banner()
prompt = Prompt()

class Cli():
    
    def __init__(self):
        self.current_user = None
        self.current_chat = None
    
    def start(self):
        self.clear(40)
        banners.welcome()
        self.clear(4)
        
        self.welcome()
        
    def welcome(self):
        print("Are you new here?")
        selection = prompt.yes_no()
        if selection == "Yes":
            self.sign_up()
        else:
            self.login()
            
    def sign_up(self):
        username = self.collect_data("What is your username?")
        if User.find_by(username=username):
            print(red("That username is taken! Please try again."))
            self.sign_up()
        else:
            password = self.collect_data("What is your password?")
            self.current_user = User.create(username=username, password=password)
        
        if self.current_user:
            self.main_menu()
        else:
            print("Please try again.\n")
            self.welcome()
    
    def collect_data(self, question):
        return prompt.ask(question)
        
    def login(self):
        username = self.collect_data("What is your username?")
        if User.find_by(username=username):
            user = User.find_by(username=username)
            password = self.collect_data("What is your password?")
            if user.password == password:
                self.current_user = user
                self.main_menu()
            else:
                print(red("That username or password was incorrect. Please try again."))
                self.welcome()
                

    def main_menu(self):
        self.clear(30)
        banners.welcome()
        print(yellow(f"Hello, {self.current_user.username}! 👋"))
        print("Please make a selection:\n")
        selection = prompt.make_menu(["My Chats", "Send a message", "Logout"])
        if selection == "My Chats":
            self.render_my_chats()
        elif selection == "Send a message":
            self.send_a_message()
        else:
            self.logout()

    def render_my_chats(self):
       pass
            
    def send_a_message(self):
        self.clear(3)
        if not self.current_chat:
            self.current_chat = Chat.create(user_id=self.current_user.id)
        user_question_input = input("Send a message:\n\n")
        question = Question.create(text=user_question_input, chat_id=self.current_chat.id)
        ai_response = controller.ask_question(question.text)
        print(ai_response)
        response = Response.create(text=ai_response["choices"][0]["message"]["content"], chat_id=self.current_chat.id)
        
        print(color(response.text).rgb_bg(68,70,84))
        print("Continue chat?")
        selection = prompt.yes_no()
        if selection == "Yes":
            self.send_a_message()
        else:
            self.main_menu()
        
    
    
    
    def logout(self):
        pass
            
        
    def clear(self, lines):
        print("\n" * lines)


cli = Cli()
cli.start()

        