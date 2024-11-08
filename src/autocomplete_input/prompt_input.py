from prompt_toolkit import prompt
from prompt_toolkit.completion import NestedCompleter
from .commands_enum import Commands


def prompt_input() -> str:
    """
    Function for using prompt commands autocomplete and returns user's input
    """

    completer = NestedCompleter.from_nested_dict(
        {
            Commands.HELLO.value: None,
            Commands.ADD_CONTACT.value: {"<name> <phone>": None},
            Commands.CHANGE_CONTACT.value: {
                "<name> <phone to change> <new phone>": None
            },
            Commands.PHONE.value: {"<name>": None},
            Commands.ADD_BIRTHDAY.value: {"<name> <birthday>": None},
            Commands.SHOW_BIRTHDAY.value: {"<name>": None},
            Commands.BIRTHDAYS.value: {"<days> optional": None},
            Commands.ADD_ADDRESS.value: {"<name> <address>": None},
            Commands.ADD_EMAIL.value: {"<name> <email>": None},
            Commands.ALL.value: None,
            Commands.ADD_NOTE.value: {"<name> <description>": None},
            Commands.SHOW_NOTES.value: None,
            Commands.SHOW_NOTE.value: {"<name>": None},
            Commands.DELETE_NOTE.value: {"<id>": None},
            Commands.EDIT_NOTE.value: {"<id> <new description>": None},
            Commands.CLOSE.value: None,
            Commands.EXIT.value: None,
        }
    )

    user_input = prompt("Enter command: ", completer=completer)
    return user_input