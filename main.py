from cli import CLI
from commands import Command
from router import Router, Route
import decorators as dc
from fields import StringField, NumberField
from ui.colors import RGB, tint_text, Tint
from ui.components import Text

class StartProject(Command):
    name = "start"
    description = "Start a new Adam project"
    fields = [
            StringField(name="project", maxl=5, description="Name of the project"),
    ]

    def command(self, args):
        txt=Text("hello world", color=Tint.OKBLUE)
        txt.show()

@dc.command(name="delete", description="Delete new adam project")
@dc.field(StringField(name="name", maxl=5, description="name of the project"))
@dc.field(StringField(name="description", maxl=5, description="description of the project"))
@dc.field(NumberField(name="number", description="number of times"))
def DeleteProject(args):
    txt=Text("delete project", color=Tint.OKBLUE)
    txt.show()

@dc.command(name="project", description="create, destroy, list projects")
def ListProject(args):
    print(tint_text("List projects", color=Tint.FAIL))

def main():
    router = Router([
            Route(
                path="project",
                help_text="Project utils",
                command=ListProject,
                children=[
                        Route(
                            path="start",
                            command=StartProject()
                        ),
                        Route(
                            path="delete",
                            command=DeleteProject
                        )
                    ],
            )]
        )

    cli = CLI(router)
    cli.run()

if __name__ == "__main__":
    main()
