from collections import UserList
from src.note import Note


class Notes(UserList):

    """
    Class for the NotesList that stores and manages all notes
    """
    ids = 0

    def add_note(self, note: Note):
        if note not in self.data:
            note.id.value = Notes.ids
            self.data.append(note)
            Notes.ids += 1

    def find_note(self, note: Note):
        if note in self.data:
            return note
        else:
            raise Exception('There is no notes like this')

    def delete(self, name: str):
        notes = list(
            filter(lambda note: note.name.value == name, self.data)
        )
        if not len(notes):
            raise Exception("invalid data format!")
        self.data.pop(notes[0])
