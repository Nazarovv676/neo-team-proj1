from src import (
    input_error,
    NoNotesFound,
    
)
from tabulate import tabulate
from src.notes import Notes

@input_error
def find_by_tag(args, notebook: Notes):
    tag, *_=args

    notes = notebook.find_note_by_tag(tag)

    if len(notes)==0:
        raise NoNotesFound()
    
    table_data = [
        (note.id.value,note.name.value, note.description, str.join("\n", map(lambda tag: tag.value, note.tags)))
        for note in notes
    ]

    return tabulate(table_data, headers=["Id","Name", "Note", "Tags"], tablefmt="grid")

