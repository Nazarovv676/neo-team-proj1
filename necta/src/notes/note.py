from src.contacts import Name
from src.fields.id import Id
from src.notes.fields.keyword import Keyword
from src.notes.fields.tag import Tag
from colorama import Fore


class Note():
    def __init__(self, name: str, description: str):
        self.id = None
        self.description = description
        self.name = Name(name)

    def __str__(self):
        return f"""Contact name: {Fore.GREEN}{self.name.value}{Fore.RESET}, \
description: {Fore.BLUE}{self.description}{Fore.RESET}"""

    def set_id(self, id: int):
        self.id = Id(id)
