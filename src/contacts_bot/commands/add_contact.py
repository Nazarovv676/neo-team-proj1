from src import (
    MESSAGES,
    input_error,
)
from src.address_book import AddressBook, Record


@input_error
def add_contact(args: list, book: AddressBook) -> str:
    name, phone, *_ = args
    record = book.find(name)
    message = MESSAGES["contact_updated"]

    if record is None:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        message = MESSAGES["contact_added"]
    else:
        record.add_phone(phone)
        # TODO: Add this message to the MESSAGES dictionary
        message = "new phone added to contact"
    return message
