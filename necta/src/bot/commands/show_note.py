from tabulate import tabulate
from src import (
    MESSAGES,
    input_error,
    NoNotesFound,
)
from src.notes import Notes


@input_error
def show_note(args, notebook: Notes) -> str:
    name, *_ = args

    notes = notebook.find_note(name)

    if len(notes) == 0:
        raise NoNotesFound()

    table_data = [
        (note.id.value,note.name.value, note.description, str.join("\n", map(lambda tag: tag.value, note.tags)))
        for note in notes
    ]

    return tabulate(table_data, headers=["Id","Name", "Note", "Tags"], tablefmt="grid")
