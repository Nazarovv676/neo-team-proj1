from tabulate import tabulate
from necta.src import (
    MESSAGES,
    input_error,
    NoContactFound,
)
from necta.src.contacts import AddressBook
from colorama import Fore


@input_error
def show_birthday(args: list, book: AddressBook) -> str:
    name, *_ = args
    record = book.find(name)
    if record is None:
        raise NoContactFound()
    return (
        MESSAGES["no_birthday"]
        if record.birthday is None
        else f"{Fore.GREEN}{record.birthday.format_birthday()}"
    )
