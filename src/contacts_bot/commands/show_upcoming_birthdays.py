from tabulate import tabulate
from src import (
    MESSAGES,
    input_error,
)
from src.address_book import AddressBook


@input_error
def show_upcoming_birthdays(book: AddressBook) -> str:
    birthdays = book.get_upcoming_birthdays()
    if not len(birthdays):
        return MESSAGES["upcoming_birthdays_empty"]

    table_data = [
        (birthday["name"], birthday["congratulation_date"]) for birthday in birthdays
    ]

    return tabulate(
        table_data, headers=["Name", "Congratulation date"], tablefmt="fancy_grid"
    )
