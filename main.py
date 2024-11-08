from src import MENU, ERROR_MESSAGES, MESSAGES, InvalidCommand, save_data, load_data
from src.address_book import AddressBook
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
    add_address,
    add_email,
)

from src.note.commands import (add_note, show_notes, show_note, delete_note, edit_note)
from src.note import Notes

def main():
    """
    This is a bot for saving, changing and reviewing phone contacts.
    """

    book = load_data("addressbook.pkl", lambda: AddressBook())
    notebook = load_data("notebook.pkl", lambda: Notes())
    print(MESSAGES["welcome"])
    print(MENU)
    while True:
        try:
            user_input = prompt_input()
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                save_data(book, "addressbook.pkl")
                save_data(notebook, "notebook.pkl")
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
                    print(show_upcoming_birthdays(args, book))
                case "add-address":
                    print(add_address(args, book))
                case "add-email":
                    print(add_email(args, book))
                case "add-note":
                    print(add_note(args, notebook))
                case "show-notes":
                    print(show_notes(notebook))
                case "show-note":
                    print(show_note(args, notebook))
                case "delete-note":
                    print(delete_note(args, notebook))
                case "edit-note":
                    print(edit_note(args, notebook))
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
