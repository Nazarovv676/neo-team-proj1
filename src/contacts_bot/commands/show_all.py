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
        (
            user.name.value,
            str.join("\n", map(lambda phone: phone.value, user.phones)),
            user.email.value if user.email else "-",
            user.address.value if user.address else "-",
            user.birthday.format_birthday() if user.birthday else "-"
        )
        for user in users
    ]

    return tabulate(table_data, headers=["Name", "Phones", "Email", "Address", "Birthday"], tablefmt="fancy_grid")
