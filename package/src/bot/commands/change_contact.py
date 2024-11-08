from src import (
    MESSAGES,
    input_error,
    NoContactFound,
)
from src.contacts import AddressBook


@input_error
def change_contact(args: list, book: AddressBook) -> str:
    name, *phones = args
    record = book.find(name)
    if record is None:
        raise NoContactFound()
    record.edit_phone(phones[0], phones[1])
    return MESSAGES["contact_updated"]
