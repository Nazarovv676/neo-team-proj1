from tabulate import tabulate
from src import (
    MESSAGES,
    input_error,
)
from src.address_book import AddressBook


@input_error
def show_all(book: AddressBook) -> str:
    if len(book) == 0:
        return MESSAGES["contacts_empty"]

    users = book.find_all()
    table_data = [
        (user.name.value, str.join("\n", map(lambda phone: phone.value, user.phones)))
        for user in users
    ]

    return tabulate(table_data, headers=["Name", "Phones"], tablefmt="fancy_grid")
