from src import MENU, ERROR_MESSAGES, MESSAGES, InvalidCommand, save_data, load_data
from src.autocomplete_input import prompt_input, Commands
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
    book = load_data()
    print(book)
    print(MESSAGES["welcome"])
    print(MENU)
    while True:
        try:
            user_input = prompt_input()
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                save_data(book)
                print(MESSAGES["bye"])
                break

            match command:
                case Commands.HELLO.value:
                    print(MESSAGES["help_question"])
                case Commands.MENU.value:
                    print(MENU)
                case Commands.ADD_CONTACT.value:
                    print(add_contact(args, book))
                case Commands.CHANGE_CONTACT.value:
                    print(change_contact(args, book))
                case Commands.PHONE.value:
                    print(show_phone(args, book))
                case Commands.ALL.value:
                    print(show_all(book))
                case Commands.ADD_BIRTHDAY.value:
                    print(add_birthday(args, book))
                case Commands.SHOW_BIRTHDAY.value:
                    print(show_birthday(args, book))
                case Commands.BIRTHDAYS.value:
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
