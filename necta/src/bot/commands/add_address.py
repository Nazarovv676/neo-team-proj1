from necta.src import (
    MESSAGES,
    ERROR_MESSAGES,
    input_error,
    NoContactFound,
    AddressException,
)
from necta.src.contacts import AddressBook

@input_error
def add_address(args: list, book: AddressBook) -> str:
    if len(args) < 2:
        raise AddressException(ERROR_MESSAGES["name_and_address_missing"])
    name, *address_parts = args
    record = book.find(name)
    if record is None:
        raise NoContactFound()
    full_address = " ".join(address_parts)
    record.add_address(full_address)
    return MESSAGES["address_added"]