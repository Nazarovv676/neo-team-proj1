from tabulate import tabulate
from src.exceptions import NotesInputException
from src import (
    MESSAGES,
    input_error,
    NoNotesFound,
)
from src.notes import Notes


@input_error
def show_note(args, notebook: Notes) -> str:
    try:
        name, *_ = args
    except:
        raise NotesInputException("Name is required!")

    notes = notebook.find_note(name)

    if len(notes) == 0:
        raise NoNotesFound()

    table_data = [
        (note.name.value, note.description, str.join(
            "\n", map(lambda tag: tag.value, note.tags)))
        for note in notes
    ]

    return tabulate(table_data, headers=["Name", "Note", "Tags"], tablefmt="fancy_grid")
