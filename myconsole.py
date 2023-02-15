from commands import Command

class StartProject(Command):
    name = "startproject"
    description = "Start a new Adam project"
    fields = [
            StringField(name="Project name", error_message="Not valid first arg", max_length=5),
            StringField(name="Project name", error_message="Not valid second arg", max_length=5)
    ]

    def command(self, args):
        print("create new project")
