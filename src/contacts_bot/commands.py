from src import (
    MESSAGES,
    input_error,
    NoContactFound,
    BirthdayException,
    ERROR_MESSAGES,
)
from src.address_book import AddressBook, Record
from colorama import Fore


@input_error
def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


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


@input_error
def change_contact(args: list, book: AddressBook) -> str:
    name, *phones = args
    record = book.find(name)
    if record is None:
        raise NoContactFound()
    record.edit_phone(phones[0], phones[1])
    return MESSAGES["contact_updated"]


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


@input_error
def show_all(book: AddressBook) -> str:
    if len(book) == 0:
        return MESSAGES["contacts_empty"]
    
    records = book.find_all()
    return '\n'.join(str(record) for record in records)


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


@input_error
def show_upcoming_birthdays(book: AddressBook) -> str:
    birthdays = book.get_upcoming_birthdays()
    if not len(birthdays):
        return MESSAGES["upcoming_birthdays_empty"]
    message_lst = [
        f"""Name: {Fore.GREEN}{birthday["name"]}{Fore.RESET}, Congrats date: {Fore.CYAN}{birthday["congratulation_date"]}{Fore.RESET}"""
        for birthday in birthdays
    ]
    return '\n'.join(message_lst)
