from utils.classes import get_subtypes
from commands import Command

class CLI():
    def __init__(self):
        self.commands = get_subtypes(Command)

    def run(self, argv):
        for x in self.commands:
            command = x()
            if(command.name == argv[1]):
                command.run(argv[2:])
                return 0
        self.help()
        return 1

    def help(self):
        print("This is the help of CLI")
        for x in self.commands:
            print(x().help_text)

