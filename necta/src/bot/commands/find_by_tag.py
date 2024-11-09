from necta.src.exceptions import NotesInputException
from src import (
    input_error,
    NoNotesFound,

)
from tabulate import tabulate
from necta.src.notes import Notes


@input_error
def find_by_tag(args, notebook: Notes):
    try:
        tag, *_ = args
    except:
        raise NotesInputException("Tag is required!")

    notes = notebook.find_note_by_tag(tag)

    if len(notes) == 0:
        raise NoNotesFound()

    table_data = [
        (note.id.value, note.name.value, note.description,
         str.join("\n", map(lambda tag: tag.value, note.tags)))
        for note in notes
    ]

    return tabulate(table_data, headers=["Id", "Name", "Note", "Tags"], tablefmt="fancy_grid")
