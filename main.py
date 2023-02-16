from cli import CLI
from commands import Command
from router import Router, Route
from fields import StringField
from ui.colors import RGB, tint_text, Tint
from ui.components import Text

class StartProject(Command):
    name = "start"
    description = "Start a new Adam project"
    fields = [
            StringField(name="Project name", error_message="Not valid first arg", max_length=5),
    ]

    def command(self, args):
        txt=Text("hello world", color=Tint.OKBLUE)
        txt.show()


class ListProject(Command):
    name = "project"
    description = "Create, List, Delete projects"

    def command(self, args):
        print(tint_text("List projects", color=Tint.FAIL))

def main():
    router = Router([
            Route(
                path="project",
                help_text="Project utils",
                command=ListProject(),
                children=[
                    Route(
                        path="start",
                        command=StartProject()
                    )
                ],
            ),
        ])

    cli = CLI(router)
    cli.run()

if __name__ == "__main__":
    main()
