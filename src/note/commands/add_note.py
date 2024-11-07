from src import (
    MESSAGES,
    input_error,
)
from src.address_book.address_book import AddressBook
from src.note import Notes, Note


@input_error
def add_note(args: list, book:AddressBook ,notes: Notes) -> str:
    name, *description = args
    message = MESSAGES["note_added"]
    description_joined = ' '.join(description)

    note = Note(name, description_joined)

    user = book.find(name)
    if user is None:
        message=MESSAGES["no_user_with_this_name"]
    else: notes.add_note(note)


    return message
