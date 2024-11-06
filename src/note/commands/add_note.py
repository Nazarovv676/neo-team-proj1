from src import (
    MESSAGES,
    input_error,
    NoContactFound,
    BirthdayException,
    ERROR_MESSAGES,
)
from src.note import Notes, Note
from colorama import Fore


@input_error
def add_note(args: list, notes: Notes) -> str:
    name, description, *_ = args
    capitalized_name = name.capitalize()
    
    note = Note(name, description)

    notes.add_note(note)

    print(list(lambda note: note, notes))
