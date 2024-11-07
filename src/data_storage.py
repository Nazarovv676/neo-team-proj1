import pickle
from src.address_book import AddressBook
from src.note.notes import Notes


def save_data(book, filename="addressbook.pkl"):
    """
    Function for saving Address Book in binary file
    """
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    """
    Function for loading Address Book from binary file
    """
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


def save_notes(notebook, filename="notebook.pkl"):
    """
    Function for saving Notes in binary file
    """
    with open(filename, "wb") as f:
        pickle.dump(notebook, f)


def load_notes(filename="notebook.pkl"):
    """
    Function for loading Notes from binary file
    """
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return Notes()
