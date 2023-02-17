from utils.classes import get_subtypes
from dataclasses import dataclass
from commands import Command
from router import Router
from ui.colors import Tint, tint_text
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
        help_text=""
        for x in node:
            if(x.command):
                help_text+=f'   {x.command.help_text}\n'
            else:
                help_text+=f'    {tint_text(x.path, Tint.OKGREEN )} : {x.help_text}\n'
        print(
        f"""
 {tint_text("Command not found", Tint.FAIL)}

 Command list:

{help_text}
        """)


