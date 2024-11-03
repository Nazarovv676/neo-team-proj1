import pickle
from src.address_book import AddressBook


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
