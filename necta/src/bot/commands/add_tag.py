from src import (
    MESSAGES,
    input_error,
    NoNotesFound
)
from src.notes import Notes
from src.autocomplete import prompt_input
from tabulate import tabulate


@input_error
def add_tag(args, notebook: Notes):
    name, tag, *_ = args
    message = MESSAGES["tag_is_added"]

    notes = notebook.find_note(name)
    if not notes:
        raise NoNotesFound()

    if len(notes) > 1:
        table_data = [
            (note.id.value, note.name.value, note.description,
             "\n".join(tag.value for tag in note.tags))
            for note in notes
        ]

        print(f"Found more than one note with name: '{name}'")
        print(tabulate(table_data, headers=[
              "Id", "Name", "Note", "Tags"], tablefmt="grid"))
        print("Enter note ID")
        note_id = int(prompt_input())
        current_note = notebook.find_note_with_id(note_id)
        if not current_note:
            raise NoNotesFound()
    else:
        current_note = notes[0]

    current_note.set_tag(tag)
    notebook.edit_note(current_note)

    return message
