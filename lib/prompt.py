from simple_term_menu import TerminalMenu
from pwinput import pwinput 
from prettycli import green, bright_red

class Prompt():
    password_attempt = 0
    
    def ask(self, question, isPassword=False):
        if isPassword:
            user_input = pwinput("Please enter your password:\n")
            if self.confirm(user_input, isPassword=True):
                return user_input
            return self.ask(question, isPassword=True)
        else:
            user_input = input(question + "\n")
            if self.confirm(user_input):
                return user_input
        return self.ask(question)
    
    def confirm(self, collected_input, isPassword=False):
        if isPassword:
            user_input = pwinput("Please confirm your password:")
            if user_input == collected_input:
                print("password confirmed")
                return True
            else: 
                print(bright_red("Passwords do not match!")," Please try again\n\n")
                return False
        else:
            print(f"You entered {green(collected_input)}\nAre you sure?\n")
            return self.yes_no() == "Yes"
        
    def yes_no(self, option=None):
        options = ["Yes", "No"]
        if option:
            options.append(option)
        return self.make_menu(options)
        
    def make_menu(self, options, option=None):
        if option:
            options.append(option)
        menu = TerminalMenu(options)
        selection = menu.show()
        return options[selection]
        
        
        