from ui.colors import Tint, tint_text
from fields import BaseField
from typing import List, Optional,Callable
from dataclasses import dataclass, field
from flags import Flag

class Command:
    fields: List[BaseField]
    command : Optional[Callable] = None
    last_multiple = False

    def __init__(self, last_multiple=False):
        self.last_multiple=last_multiple

    def validate(self, args):
        #FIXME: Refactor this code is fucking shit
        if not self.last_multiple:
            if(len(args) < len(self.fields)):
                self.usage("You have missing arguments")
                return False
            if(len(args) > len(self.fields)):
                self.usage("Too much arguments")
                return False

        for x in range(0, len(args)):
            #FIXME: refactor this.
            #this is making that if last_multiple is true accept last values wihout exceed field array index
            field_index = x
            if self.last_multiple and x > (len(self.fields) - 1):
                field_index = len(self.fields) - 1
            if not self.fields[field_index].is_valid(args[x], throw_exception=True):
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
