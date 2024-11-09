from necta.src.constants import ERROR_MESSAGES
from necta.src.exceptions import NoteException
from .note import Note
from collections import UserList
from fuzzywuzzy import fuzz


class Notes(UserList):

    """
    Class for the NotesList that stores and manages all notes
    """
    _id = 0

    def add_note(self, note: Note):
        if note not in self.data:
            note.set_id(self._id)
            self._id += 1
            self.data.append(note)

    def edit_note(self, current_note: Note):
        counter = 0
        for note in self.data:
            if note.id.value == current_note.id.value:
                break
            counter += 1
        
        if counter == len(self.data):
            raise NoteException(ERROR_MESSAGES["note_not_found"])
        
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

    def delete(self, id: int) -> bool:
        current_note = None
        for note in self.data:
            if (note.id.value == id):
                current_note = note
        self.data.remove(current_note)
        return current_note

    def find_note_by_tag(self, tag:str)-> list:
        notes=[]
        for note in self.data:
            for current_tag in note.tags:
                if tag in current_tag.value:
                    notes.append(note)
                    break
        
        return notes
    
    def search(self, query: str, threshold: int = 60) -> list:
        """Searches for notes by a given query. Checks name and description."""
        results = []
        for note in self.data:
            if fuzz.partial_ratio(query, note.name.value) >= threshold:
                results.append(note)
            elif fuzz.partial_ratio(query, note.description) >= threshold:
                results.append(note)
        return results
    
    
