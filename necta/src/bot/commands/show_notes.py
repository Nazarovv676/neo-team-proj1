from tabulate import tabulate
from necta.src import (
    MESSAGES,
    input_error,
)
from necta.src.notes import Notes


@input_error
def show_notes(notebook: Notes) -> str:
    if len(notebook) == 0:
        return MESSAGES["notes_empty"]

    notes = notebook.find_all()
    table_data = [
        (note.name.value, note.description)
        for note in notes
    ]

    return tabulate(table_data, headers=["Name", "Note"], tablefmt="fancy_grid")
