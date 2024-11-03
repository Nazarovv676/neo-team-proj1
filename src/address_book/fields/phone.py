from src.address_book import Field
from src import PhoneException, ERROR_MESSAGES
import re


class Phone(Field):
    """
    Class for record's Phone field
    """

    def __init__(self, phone: str):
        validated_phone = self.__validate_phone_number(phone)
        super().__init__(validated_phone)

    def __validate_phone_number(self, phone: str):
        phone_pattern = re.compile(r"[^0-9+]")
        if re.search(phone_pattern, phone):
            raise PhoneException(ERROR_MESSAGES["phone_only_num"])
        if len(phone) != 10:
            raise PhoneException(ERROR_MESSAGES["phone_length"])
        return phone

    def __str__(self) -> str:
        return super().__str__()
