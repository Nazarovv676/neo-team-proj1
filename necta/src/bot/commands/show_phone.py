from src import (
    MESSAGES,
    input_error,
    NoContactFound,
)
from src.contacts import AddressBook
from colorama import Fore


@input_error
def show_phone(args: list, book: AddressBook) -> str:
    name, *_ = args
    record = book.find(name)
    if record is None:
        raise NoContactFound()
    if not len(record.phones):
        return MESSAGES["no_phone_exists"]
    phones = [phone.value for phone in record.phones]
    return f"{Fore.BLUE}{'; '.join(phones)}"
