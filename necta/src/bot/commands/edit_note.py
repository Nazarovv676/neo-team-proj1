from necta.src import (
    MESSAGES,
    input_error,
)
from necta.src.bot.commands.notes_table import notes_table
from necta.src.exceptions import NotesInputException
from necta.src.notes import Notes


@input_error
def edit_note(args, notebook: Notes):
    try:
        name, *description = args
    except:
        raise NotesInputException("Name and description are required!")

    description_joined = ' '.join(description)
    message = MESSAGES['note_is_updates']

    note = notes_table(name, notebook)

    note.description = description_joined

    notebook.edit_note(note)

    return message
