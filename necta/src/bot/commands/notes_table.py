from necta.src.notes.notes import Notes
from necta.src.notes.note import Note
from necta.src.exceptions import NoNotesFound
from necta.src.autocomplete import prompt_input
from tabulate import tabulate


def notes_table(name: str, notebook: Notes) -> Note:
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
              "Id", "Name", "Note", "Tags"], tablefmt="fancy_grid"))
        note_id = int(input("Enter note ID: "))
        current_note = notebook.find_note_with_id(note_id)
        if not current_note:
            raise NoNotesFound()
        if not current_note in notes:
            raise NoNotesFound()
    else:
        current_note = notes[0]
    if current_note is None:
        raise NoNotesFound()
    return current_note
