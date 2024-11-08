from src import (
    MESSAGES,
    input_error,
)
from src.address_book.address_book import AddressBook
from src.note import Notes, Note


@input_error
def add_note(args: list, notes: Notes) -> str:
    name, *description = args
    message = MESSAGES["note_added"]
    description_joined = ' '.join(description)

    note = Note(name, description_joined)
    notes.add_note(note)

    return message
