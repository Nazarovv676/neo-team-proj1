from src import (
    MESSAGES,
    ERROR_MESSAGES,
    input_error,
    NoContactFound,
    NameException,
)
from src.contacts import AddressBook

@input_error
def delete_contact(args: list, book: AddressBook) -> str:
    if len(args) < 1:
        raise NameException(ERROR_MESSAGES["name_missing"])
    
    name = args[0]

    record = book.find(name)
    
    if record is None:
        raise NoContactFound()
    
    book.delete_record(record)
    return MESSAGES["contact_deleted"]