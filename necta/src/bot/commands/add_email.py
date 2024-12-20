from necta.src import (
    MESSAGES,
    ERROR_MESSAGES,
    input_error,
    NoContactFound,
    EmailException,
)
from necta.src.contacts import AddressBook

@input_error
def add_email(args: list, book: AddressBook) -> str:
    if len(args) < 2:
        raise EmailException(ERROR_MESSAGES["name_and_email_missing"])
    
    name, email, *_ = args
    record = book.find(name)
    if record is None:
        raise NoContactFound()
    record.add_email(email)
    return MESSAGES["email_added"]