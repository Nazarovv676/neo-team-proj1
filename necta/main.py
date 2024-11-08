from src import MENU, ERROR_MESSAGES, MESSAGES, InvalidCommand, save_data, load_data
from src.contacts import AddressBook
from src.autocomplete import prompt_input, Commands
from src.bot import (
    parse_input,
    add_contact,
    change_contact,
    show_phone,
    show_all,
    add_birthday,
    show_birthday,
    show_upcoming_birthdays,
    add_address,
    add_email,
    delete_contact,
    add_note,
    show_notes,
    show_note,
    delete_note,
    edit_note,
    add_phone
)
from src.notes import Notes

ADDRESS_BOOK_FILEPATH = "addressbook.pkl"
NOTEBOOK_FILEPATH = "notebook.pkl"

def main():
    """
    This is a bot for saving, changing and reviewing phone contacts.
    """

    book = load_data(ADDRESS_BOOK_FILEPATH, lambda: AddressBook())
    notebook = load_data(NOTEBOOK_FILEPATH, lambda: Notes())
    print(MESSAGES["welcome"])
    print(MENU)
    while True:
        try:
            user_input = prompt_input()
            command, *args = parse_input(user_input)

            if command in [Commands.CLOSE.value, Commands.EXIT.value]:
                save_data(book, ADDRESS_BOOK_FILEPATH)
                save_data(notebook, NOTEBOOK_FILEPATH)
                print(MESSAGES["bye"])
                break

            match command:
                case Commands.HELLO.value:
                    print(MESSAGES["help_question"])
                case Commands.MENU.value:
                    print(MENU)
                case Commands.ADD_CONTACT.value:
                    print(add_contact(args, book))
                case Commands.ADD_PHONE.value:
                    print(add_phone(args, book))
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
                    print(show_upcoming_birthdays(args, book))
                case Commands.ADD_ADDRESS.value:
                    print(add_address(args, book))
                case Commands.ADD_EMAIL.value:
                    print(add_email(args, book))
                case Commands.ADD_NOTE.value:
                    print(add_note(args, notebook))
                case Commands.SHOW_NOTES.value:
                    print(show_notes(notebook))
                case Commands.SHOW_NOTE.value:
                    print(show_note(args, notebook))
                case Commands.DELETE_NOTE.value:
                    print(delete_note(args, notebook))
                case Commands.EDIT_NOTE.value:
                    print(edit_note(args, notebook))
                case Commands.DELETE_CONTACT.value:
                    print(delete_contact(args, book))
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
