from src import MENU, ERROR_MESSAGES, MESSAGES, InvalidCommand
from src.address_book import AddressBook
from src.contacts_bot import (
    parse_input,
    add_contact,
    change_contact,
    show_phone,
    show_all,
    add_birthday,
    show_birthday,
    show_upcoming_birthdays,
)


def main():
    """
    This is a bot for saving, changing and reviewing phone contacts.
    """
    book = AddressBook()
    print(MESSAGES["welcome"])
    print(MENU)
    while True:
        try:
            user_input = input(MESSAGES["enter_command"])
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print(MESSAGES["bye"])
                break

            match command:
                case "hello":
                    print(MESSAGES["help_question"])
                case "menu":
                    print(MENU)
                case "add":
                    print(add_contact(args, book))
                case "change":
                    print(change_contact(args, book))
                case "phone":
                    print(show_phone(args, book))
                case "all":
                    show_all(book)
                case "add-birthday":
                    print(add_birthday(args, book))
                case "show-birthday":
                    print(show_birthday(args, book))
                case "birthdays":
                    print(show_upcoming_birthdays(book))
                case _:
                    raise InvalidCommand(ERROR_MESSAGES["invalid_command"])

        except InvalidCommand as e:
            print(e)
            continue


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
