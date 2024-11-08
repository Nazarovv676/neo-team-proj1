from src import MENU, ERROR_MESSAGES, MESSAGES, InvalidCommand, save_data, load_data
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
            user_input = input(MESSAGES["enter_command"])
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                save_data(book)
                save_notes(notebook)
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
