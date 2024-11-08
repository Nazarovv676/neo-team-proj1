from src import (
    MESSAGES,
    ERROR_MESSAGES,
    input_error,
    NoContactFound,
    NameException,
)
from src.address_book import AddressBook

@input_error
def delete_contact(args: list, book: AddressBook) -> str:
    if len(args) < 1:
        raise NameException(ERROR_MESSAGES["name_missing"])
    name = args[0]
    book.delete_record(name)
    return MESSAGES["contact_deleted"]