import string


class File():
    name: string

    def __init__(self, file):
        self.name = file["name"]
