from cli import CLI
from commands import Command
from router import Router, Route
from fields import StringField

class StartProject(Command):
    name = "startproject"
    description = "Start a new Adam project"
    fields = [
            StringField(name="Project name", error_message="Not valid first arg", max_length=5),
    ]

    def command(self, args):
        print("create new project")

def main():
    router = Router([
            Route(
                path="project",
                help_text="Project utils",
                children=[
                    Route(
                        path="start",
                        command=StartProject()
                    )
                ]
            )
        ])

    cli = CLI(router)
    cli.run()

if __name__ == "__main__":
    main()
