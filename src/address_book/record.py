from src.address_book import Name, Phone, Birthday
from src import PhoneException, ERROR_MESSAGES
from colorama import Fore


class Record:
    """
    Class for the Record in the Address Book
    """

    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __str__(self):
        return f"""Contact name: {Fore.GREEN}{self.name.value}{Fore.RESET}, \
phones: {Fore.BLUE}{'; '.join(p.value for p in self.phones) if len(self.phones) else '- '}{Fore.RESET}, \
birthday: {Fore.CYAN}{self.birthday.format_birthday() if self.birthday else '-'}{Fore.RESET}"""

    def add_phone(self, phone: str):
        if phone in [phone.value for phone in self.phones]:
            raise PhoneException(ERROR_MESSAGES["phone_already_exists"])
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phones = [p.value for p in self.phones]
        phone_index = phones.index(phone)
        self.phones.pop(phone_index)

    def edit_phone(self, *args):
        phones = [p.value for p in self.phones]
        try:
            old_phone_idx = phones.index(args[0])
            self.phones.insert(old_phone_idx, Phone(args[1]))
            self.remove_phone(args[0])
        except ValueError:
            raise PhoneException(ERROR_MESSAGES["no_phone"])

    def find_phone(self, phone: str):
        for record_phone in self.phones:
            if record_phone.value == phone:
                return record_phone.value
        return ERROR_MESSAGES["no_phone"]

    def add_birthday(self, birthday: str):
        self.birthday = Birthday(birthday)
