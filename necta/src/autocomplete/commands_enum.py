from enum import Enum


class Commands(Enum):
    HELLO = "hello"
    MENU = "menu"
    ADD_CONTACT = "add"
    ADD_PHONE = "add-phone"
    CHANGE_CONTACT = "change"
    PHONE = "phone"
    ALL = "all"
    ADD_BIRTHDAY = "add-birthday"
    SHOW_BIRTHDAY = "show-birthday"
    BIRTHDAYS = "birthdays"
    ADD_ADDRESS = "add-address"
    ADD_EMAIL = "add-email"
    ADD_NOTE = "add-note"
    SHOW_NOTES = "show-notes"
    SHOW_NOTE = "show-note"
    DELETE_NOTE = "delete-note"
    EDIT_NOTE = "edit-note"
    ADD_NOTE_TAG="add-note-tag"
    FIND_NOTE_BY_TAG="find-notes-by-tag"
    DELETE_CONTACT = "delete-contact"
    CLOSE = "close"
    EXIT = "exit"


def get_commands_list() -> list[Commands]:
    """Function that return the list of enum values"""
    return [command.value for command in list(Commands)]
