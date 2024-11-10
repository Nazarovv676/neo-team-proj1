from tabulate import tabulate
from necta.src.constants import ERROR_MESSAGES
from necta.src.contacts.address_book import AddressBook
from necta.src.exceptions import SearchException, input_error
from necta.src.notes.notes import Notes

@input_error
def search(args: list[str], address_book: AddressBook, notebook: Notes) -> str:
    if len(args) < 1:
        raise SearchException(ERROR_MESSAGES["search_query_missing"])
    
    query = args[0]
    contacts = address_book.search(query)
    notes = notebook.search(query)
    
    contacts_data = [
        (
            contact.name.value,
            str.join("\n", map(lambda phone: phone.value, contact.phones)),
        )
        for contact in contacts
    ]
    
    notes_data = [
        (note.name.value, note.description) for note in notes
    ]
    
    contacts_table = tabulate(contacts_data, headers=["Name", "Phones"], tablefmt="fancy_grid") if len(contacts) > 0 else "No contacts found"
    notes_table = tabulate(notes_data, headers=["Name", "Description"], tablefmt="fancy_grid") if len(notes) > 0 else "No notes found"
    
    return f"Contacts\n{contacts_table}\n\nNotes\n{notes_table}"