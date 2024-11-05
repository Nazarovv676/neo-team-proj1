from collections import UserDict
from src.note import Note


class NotesList(UserDict):

    """
    Class for the NotesList that stores and manages all notes
    """

    notes = 0

    def add_note(self, note: Note):
        self.data[note] = NotesList.notes
        NotesList.notes += 1

    def delete(self, name: str):
        notes = list(
            filter(lambda note: note.name.value == name, self.data.keys())
        )
        if not len(notes):
            raise Exception("invalid data format!")
        self.data.pop(notes[0])
        NotesList.notes -= 1
