from necta.src.exceptions import NotesInputException
from necta.src.bot.commands.notes_table import notes_table
from necta.src import (
    MESSAGES,
    input_error,
)
from necta.src.notes import Notes


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
