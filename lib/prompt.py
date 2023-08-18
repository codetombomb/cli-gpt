from simple_term_menu import TerminalMenu
from prettycli import green

class Prompt():
    
    def ask(self, question):
        user_input = input(question + "\n")
        if self.confirm(user_input):
            return user_input
        else:
            return self.ask(question)
    
    def confirm(self, input):
        print(f"You entered {green(input)}\nAre you sure?\n")
        return self.yes_no() == "Yes"
        
    def yes_no(self):
        return self.make_menu(["Yes", "No"])
        
    def make_menu(self, options):
        menu = TerminalMenu(options)
        selection = menu.show()
        return options[selection]
        
        
        