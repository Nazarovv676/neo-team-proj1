from .note import Note
from collections import UserList


class Notes(UserList):

    """
    Class for the NotesList that stores and manages all notes
    """
    ids = 0
    first_open = True  # Атрибут класу для перевірки першого додавання

    def add_note(self, note: Note):
        if note not in self.data:
            if len(self.data) == 0 and Notes.first_open:
                current_id = 0
            else:
                current_id = self.data[-1].id.value + 1

            note.set_id(current_id)
            self.data.append(note)

            Notes.ids = current_id + 1

            Notes.first_open = False

    def edit_note(self, current_note: Note) -> bool:
        counter = 0
        for note in self.data:
            if note.id.value == current_note.id.value:
                break
            counter += 1
        self.data[counter] = current_note

    def find_note(self, name: str) -> list:
        notes = []
        for note in self.data:
            if (note.name.value == name):
                notes.append(note)
        return notes

    def find_note_with_id(self, id: int) -> Note:
        current_note = None
        for note in self.data:
            if (note.id.value == id):
                current_note = note
        return current_note

    def find_all(self):
        """Retrieves all users in the notebook."""
        return self.data

    def delete(self, id:int) -> bool:
        current_note = None
        for note in self.data:
            if (note.id.value == id):
                current_note = note
        self.data.remove(current_note)
        return current_note
