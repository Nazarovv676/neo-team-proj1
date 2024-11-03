from datetime import datetime
from src.address_book import Field
from src import ERROR_MESSAGES, BirthdayException


class Birthday(Field):
    """
    Class for record's Birthday field
    """

    def __init__(self, value):
        birthday = self.__validate_birthday(value)
        super().__init__(birthday)

    def __validate_birthday(self, value):
        try:
            return datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise BirthdayException(ERROR_MESSAGES["invalid_date_format"])

    def format_birthday(self):
        return self.value.strftime("%d.%m.%Y")
