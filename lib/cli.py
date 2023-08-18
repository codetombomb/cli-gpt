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
        
        return self.welcome()
        
    def welcome(self):
        print("Are you new here?")
        selection = prompt.yes_no(option="Exit")
        if selection == "Yes":
            self.sign_up()
        elif selection == "Exit":
            self.exit()
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
                return self.main_menu()
            else:
                print(red("That username or password was incorrect. Please try again."))
                return self.welcome()
                

    def main_menu(self):
        self.clear(30)
        banners.welcome()
        print(yellow(f"Hello, {self.current_user.username}! 👋"))
        print("Please make a selection:\n")
        selection = prompt.make_menu(["Saved Chats", "New Chat", "Logout"])
        if selection == "Saved Chats":
            return self.render_my_chats()
        elif selection == "New Chat":
            return self.send_a_message()
        else:
            return self.logout()

    def render_my_chats(self):
        if len(self.current_user.chats) == 0:
            print(yellow("You don't have any saved chats.\n"))
            time.sleep(2)
            return self.main_menu()
        else:
            self.set_current_chat()
            if self.current_chat:
                self.render_chat_conversation()
                return self.send_a_message()
    
    def render_chat_conversation(self):
        questions = self.current_chat.questions
        responses = self.current_chat.responses
        for index in range(len(questions)):
            print(questions[index].text)
            print(color(responses[index].text).rgb_bg(68,70,84))
        return
        
    def set_current_chat(self):
        print("Please select a chat:\n")
        options = Chat.all_descriptions_for(self.current_user.id)
        selection = prompt.make_menu(options, option="Back")
        if selection == "Back":
            return self.main_menu()
        self.current_chat = Chat.find_by(description=selection[2:])
        return 
            
    def send_a_message(self):
        self.clear(3)
        if not self.current_chat:
            self.current_chat = Chat.create(user_id=self.current_user.id)
        user_question_input = input("Send a message:\n\n")
        question = Question.create(text=user_question_input, chat_id=self.current_chat.id)
        ai_response = controller.ask_question(question.text)
        response = Response.create(text=ai_response["choices"][0]["message"]["content"], chat_id=self.current_chat.id)
        
        self.clear(2)
        print(color(response.text).rgb_bg(68,70,84))
        print("Continue chat?\n")
        selection = prompt.yes_no()
        if selection == "Yes":
            return self.send_a_message()
        else:
            self.current_chat.description = self.current_chat.questions[0].text[0:15] + "..."
            self.current_chat.save()
            self.current_chat = None
            return self.main_menu()
        
    
    
    
    def logout(self):
        print(color(f"Goodbye, {self.current_user.username}! 👋").rgb_bg(26,195,125))
        self.current_chat = None
        self.current_user = None
    
    def exit(self):
        pass
            
        
    def clear(self, lines):
        print("\n" * lines)


cli = Cli()
cli.start()

        