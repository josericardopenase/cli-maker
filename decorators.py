from typing import Any
from commands import Command
from fields import BaseField

def command(last_multiple : bool = False):
    #FIXME: THIS IS SHITTY CODE
    def decorator(fun):
        new_command = Command(last_multiple=last_multiple)
        if(isinstance(fun, dict)):
            new_command.fields=fun["fields"]
            new_command.command=fun["command"]
        else:
            new_command.fields=[]
            new_command.command=fun
        return new_command
    return decorator

def field(field : BaseField):
    #FIXME: THIS IS SNITTY CODE
    def decorator(fun, *args, **kargs):
        if not isinstance(fun, dict):
            return {
                    "command" : fun,
                    "fields" : [field]
            }
        else:
            return {
                    "command" : fun["command"],
                    "fields" : [field, *fun["fields"]]
            }
    return decorator
