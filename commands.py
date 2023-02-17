from ui.colors import Tint, tint_text
from fields import BaseField
from typing import List, Optional,Callable
from dataclasses import dataclass
from flags import Flag

class Command:
    name : str
    description: Optional[str] = ""
    fields: List[BaseField]
    command : Optional[Callable] = None

    def validate(self, args):
        #FIXME: Refactor this code is fucking shit
        if(len(args) < len(self.fields)):
            self.usage("You have missing arguments")
            return False
        if(len(args) > len(self.fields)):
            self.usage("Too much arguments")
            return False
        for x in range(0, len(args)):
            if not self.fields[x].is_valid(args[x], throw_exception=True):
                return False
        return True

    def usage(self,error_message : str):
        #FIXME: Refactor this code is fucking shit
        number = 1
        usage=""
        for x in self.fields:
            usage += f"     {number}. {tint_text(x.name, Tint.OKGREEN)} ({str(x)}): {x.description}\n"
            number+=1

        print(f"""
 {tint_text(error_message, Tint.FAIL)}

 Args:

{usage}
        """)

    def run(self, args):
        if(self.validate(args)):
            self.command(args)

    def command(self, args):
        if(self.command):
            self.command(args)

    @property
    def help_text(self):
        return "{} : {}".format(tint_text(self.name, Tint.OKGREEN), self.description)
