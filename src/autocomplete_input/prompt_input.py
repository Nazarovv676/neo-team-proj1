from prompt_toolkit import prompt
from prompt_toolkit.completion import NestedCompleter
from src.autocomplete_input.commands_enum import Commands


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
            Commands.BIRTHDAYS.value: {"<name>": None},
            Commands.ALL.value: None,
            Commands.CLOSE.value: None,
            Commands.EXIT.value: None,
        }
    )

    user_input = prompt("Enter command: ", completer=completer)
    return user_input
