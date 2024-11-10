from src.exceptions import NotesInputException
from src import (
    MESSAGES,
    input_error,
)
from src.notes import Notes, Note


@input_error
def add_note(args: list, notes: Notes) -> str:
    try:
        name, *description = args
    except:
        raise NotesInputException("Name and description are required!")
    message = MESSAGES["note_added"]
    description_joined = ' '.join(description)

    note = Note(name, description_joined)
    notes.add_note(note)

    return message
