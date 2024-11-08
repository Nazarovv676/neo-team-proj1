from src import (
    MESSAGES,
    input_error,
    NoContactFound,
    BirthdayException,
    ERROR_MESSAGES,
)
from src.contacts import AddressBook


@input_error
def add_birthday(args: list, book: AddressBook) -> str:
    if len(args) < 2:
        raise BirthdayException(ERROR_MESSAGES["name_and_birthday_missing"])
    name, birthday, *_ = args
    record = book.find(name)
    if record is None:
        raise NoContactFound()
    record.add_birthday(birthday)
    return MESSAGES["birthday_added"]
