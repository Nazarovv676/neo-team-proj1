from src import (
    MESSAGES,
    input_error,
    NoNotesFound
)
from src.note import Notes


@input_error
def delete_note(args, notebook: Notes):
    message = MESSAGES["note_deleted"]
    id, *_ = args

    deleted_note = notebook.delete(int(id))

    if delete_note is None:
        raise NoNotesFound()

    return message
