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
        
        
        