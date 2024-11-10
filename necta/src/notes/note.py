from necta.src.contacts import Name
from necta.src.exceptions import TagException
from necta.src.fields.id import Id
from necta.src.notes.fields.keyword import Keyword
from necta.src.notes.fields.tag import Tag
from colorama import Fore


class Note():
    def __init__(self, name: str, description: str):
        self.id = None
        self.description = description
        self.name = Name(name)
        self.tags=[]

    def __str__(self):
        return f"""Contact name: {Fore.GREEN}{self.name.value}{Fore.RESET}, \
description: {Fore.BLUE}{self.description}{Fore.RESET}"""

    def set_id(self, id: int):
        self.id = Id(id)
    
    def set_tag(self, tag: str):
        if tag in [tag.value for tag in self.tags]:
            raise TagException("This tag exists!")
        self.tags.append(Tag(tag))
