from utils.classes import get_subtypes
from dataclasses import dataclass
from commands import Command
from router import Router
from sys import argv

class CLI():
    def __init__(self, router : Router):
        self.router = router

    def run(self):
        #FIXME: this is very bad and late algorithm.
        current_route = self.router
        for index in range(1, len(argv)):
            for child in current_route:
                if child.path == argv[index]:
                    if child.is_leave:
                        child.command.run(argv[index+1:])
                        return True
                    else:
                        if child.command and (len(argv) - 1 == index):
                            child.command.run(argv[index+1:])
                            return True
                        else:
                            current_route = child
        self.help(current_route)
        return False

    def help(self, node):
        for x in node:
            if(x.command):
                print(x.command.help_text)
            else:
                print('{} : {}'.format(x.path, x.help_text))


