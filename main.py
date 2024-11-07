from src import MENU, ERROR_MESSAGES, MESSAGES, InvalidCommand, save_data, load_data
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

from src.note.commands.add_note import add_note
from src.note import Note, Notes


def main():
    """
    This is a bot for saving, changing and reviewing phone contacts.
    """
    book = load_data()
    notebook = Notes()
    print(book)
    print(MESSAGES["welcome"])
    print(MENU)
    while True:
        try:
            user_input = input(MESSAGES["enter_command"])
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                save_data(book)
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
                    print(show_all(book))
                case "add-birthday":
                    print(add_birthday(args, book))
                case "show-birthday":
                    print(show_birthday(args, book))
                case "birthdays":
                    print(show_upcoming_birthdays(args, book))
                case "note":
                    add_note(args, notebook)
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
