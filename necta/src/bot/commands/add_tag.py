from src.exceptions import NotesInputException
from src.bot.commands.notes_table import notes_table
from src import (
    MESSAGES,
    input_error,
)
from src.notes import Notes


@input_error
def add_tag(args, notebook: Notes):
    try:
        name, tag, *_ = args
    except:
        raise NotesInputException("Name and tag are required!")
    message = MESSAGES["tag_is_added"]

    note = notes_table(name, notebook)

    note.set_tag(tag)
    notebook.edit_note(note)

    return message
