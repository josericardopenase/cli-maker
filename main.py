from cli import CLI
from commands import Command
from router import Router, Route
import decorators as dc
from fields import StringField, NumberField, EmailField, FileField
from ui.colors import RGB, tint_text, Tint
from ui.components import Text

class StartProject(Command):
    fields = [
            StringField(name="project", maxl=5, description="Name of the project"),
    ]

    def command(self, args):
        txt=Text("hello world", color=Tint.OKBLUE)
        txt.show()

@dc.command()
def ListProject(args):
    print(tint_text("List projects", color=Tint.FAIL))


@dc.command()
def holaJavs(args):
    print(tint_text("Hola javs", color=Tint.OKGREEN))

@dc.command()
def holaMaria(args):
    print("hola maria")

@dc.command(last_multiple=True)
@dc.field(FileField(name="file"))
def newMaria(args):
    txt=Text(f"empezar marias llamadas {args[0]}", color=Tint.OKBLUE)
    txt.show()

def main():
    router = Router([
        Route(
                path="maria",
                help_text="hola maria",
                children=[
                    Route(
                        path="start",
                        help_text="new maria",
                        command=newMaria

                        )
                    ],
                command=holaMaria
                )
        ,
            Route(
                path="javs",
                help_text="hola javs command",
                command=holaJavs
                )
        ,
            Route(
                path="project",
                help_text="Project utils",
                children=[
                        Route(
                            path="start",
                            command=StartProject()
                        ),
                    ],
            )]
        )

    cli = CLI(router)
    cli.run()

if __name__ == "__main__":
    main()
