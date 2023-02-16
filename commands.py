from fields import BaseField
from typing import List
from abc import ABC

class Command(ABC):
    name : str
    fields: List[BaseField] = []

    def validate(self, args):
        if(len(args) != len(self.fields)):
            print("too much arguments")
            return False
        for x in range(0, len(args)):
            if not self.fields[x].is_valid(args[x], throw_exception=True):
                return False
        return True

    def run(self, args):
        if(self.validate(args)):
            self.command(args)

    def command(self, args):
        pass

    @property
    def help_text(self):
        return "{} : {}".format(self.name, self.description)
