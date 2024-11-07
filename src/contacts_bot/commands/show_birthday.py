from tabulate import tabulate
from src import (
    MESSAGES,
    input_error,
    NoContactFound,
)
from src.address_book import AddressBook
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
