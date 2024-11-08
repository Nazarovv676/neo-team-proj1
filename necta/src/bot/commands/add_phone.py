from src.contacts import AddressBook
from src.exceptions import PhoneException, NoContactFound
from src.constants import MESSAGES, ERROR_MESSAGES


def add_phone(args: list, book: AddressBook) -> str:
    if len(args) < 2:
        raise PhoneException(ERROR_MESSAGES["name_and_phone_missing"])
    
    name, phone, *_ = args
    
    record = book.find(name)
    if record is None:
        raise NoContactFound()
    
    record.add_phone(phone)
    
    return MESSAGES["phone_added"]