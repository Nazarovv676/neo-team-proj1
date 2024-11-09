from necta.src.exceptions import NotesInputException
from necta.src.bot.commands.notes_table import notes_table
from necta.src import (
    MESSAGES,
    input_error,
    NoNotesFound
)
from necta.src.notes import Notes


@input_error
def delete_note(args, notebook: Notes):
    message = MESSAGES["note_deleted"]
    try:
        name, *_ = args
    except:
        raise NotesInputException("Name is required!")

    note = notes_table(name, notebook)

    deleted_note = notebook.delete(note.id.value)

    if delete_note is None:
        raise NoNotesFound()

    return message
