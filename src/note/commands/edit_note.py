from src import (
    MESSAGES,
    input_error,
    NoNotesFound
)
from src.note import Notes

@input_error
def edit_note(args,notebook:Notes):
    id, *description=args
    description_joined = ' '.join(description)
    message=MESSAGES['note_is_updates']

    note = notebook.find_note_with_id(int(id))
    if note is None: 
        raise NoNotesFound()
    note.description=description_joined
    
    notebook.edit_note(note)

    return message
    
