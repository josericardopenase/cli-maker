from commands import Command
from fields import BaseField

def command(name : str = "", description : str = ""):
    def decorator(fun):
        new_command = Command()
        new_command.name=name
        new_command.description=description
        if(isinstance(fun, dict)):
            new_command.fields=fun["fields"]
            new_command.command=fun["command"]
        else:
            new_command.command=fun
        return new_command
    return decorator

def field(field : BaseField):
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
