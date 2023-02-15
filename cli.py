from utils.classes import get_subtypes
from dataclasses import dataclass
from commands import Command
from router import Router
from sys import argv

class CLI():
    def __init__(self, router : Router):
        self.router = router

    def run(self):
        current_route = self.router
        for index in range(1, len(argv)):
            for child in current_route:
                if child.path == argv[index]:
                    if child.is_leave:
                        child.command.run(argv[index+1:])
                    else:
                        current_route = child
