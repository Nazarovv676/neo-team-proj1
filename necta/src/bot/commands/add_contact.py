from src import NameException, ERROR_MESSAGES
from src import (
    MESSAGES,
    input_error,
)
from src.contacts import AddressBook, Record


@input_error
def add_contact(args: list, book: AddressBook) -> str:
    if len(args) < 2:
        raise NameException(ERROR_MESSAGES["name_and_phone_missing"])
    
    name, phone, *_ = args
    
    record = Record(name)
    record.add_phone(phone)
    book.add_record(record)

    return MESSAGES["contact_added"]
