from necta.src.contacts import AddressBook
from necta.src.exceptions import PhoneException, NoContactFound, input_error
from necta.src.constants import MESSAGES, ERROR_MESSAGES

@input_error
def add_phone(args: list, book: AddressBook) -> str:
    if len(args) < 2:
        raise PhoneException(ERROR_MESSAGES["name_and_phone_missing"])
    
    name, phone, *_ = args
    
    record = book.find(name)
    if record is None:
        raise NoContactFound()
    
    record.add_phone(phone)
    
    return MESSAGES["phone_added"]