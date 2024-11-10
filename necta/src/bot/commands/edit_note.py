from src import (
    MESSAGES,
    input_error,
    NoNotesFound
)
from src.autocomplete import prompt_input
from tabulate import tabulate
from src.notes import Notes


@input_error
def edit_note(args, notebook: Notes):
    name, *description = args
    description_joined = ' '.join(description)
    message = MESSAGES['note_is_updates']

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
        if not current_note in notes:
            raise NoNotesFound()
    else:
        current_note = notes[0]

    note = notebook.find_note_with_id(current_note.id.value)
    if note is None:
        raise NoNotesFound()
    note.description = description_joined

    notebook.edit_note(note)

    return message
