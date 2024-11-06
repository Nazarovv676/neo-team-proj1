from src.address_book import Name
from src.note.fields import Id, Keyword, Tag
from colorama import Fore


class Note():
    def __init__(self, name: str):
        self.id = Id()
        self.keywords = []
        self.tags = []
        self.name = Name(name)

    def __str__(self):
        return f"""Contact name: {Fore.GREEN}{self.name.value}{Fore.RESET}, \
keywords: {Fore.BLUE}{'; '.join(k.value for k in self.keywords) if len(self.keywords) else '- '}{Fore.RESET}, \
tags: {Fore.CYAN}{'; '.join(t.value for t in self.tags) if len(self.tags) else '- '}{Fore.RESET}"""

    def add_keyword(self, keyword):
        if keyword in [keyword.value for keyword in self.keywords]:
            raise Exception("This keyword exists!")
        self.keywords.append(Keyword(keyword))

    def remove_keyword(self, keyword):
        keywords = [k.value for k in self.keywords]
        keyword_index = keywords.index(keyword)
        self.keywords.pop(keyword_index)

    def add_tag(self, tag):
        if tag in [tag.value for tag in self.tags]:
            raise Exception("This tag exists!")
        self.tags.append(Tag(tag))

    def remove_tag(self, tag):
        tags = [t.value for t in self.tags]
        tag_index = tags.index(tag)
        self.tags.pop(tag_index)
