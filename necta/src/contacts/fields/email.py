from datetime import datetime
from necta.src import EmailException, ERROR_MESSAGES
import re

from necta.src.fields.field import Field

class Email(Field):
    """
    Class for record's Email field
    """
    def __init__(self, email: str):
        validated_email = self.__validate_email(email)
        super().__init__(validated_email)

    def __validate_email(self, email: str):
        email_pattern = re.compile(r"^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$")
        if not re.match(email_pattern, email):
            raise EmailException(ERROR_MESSAGES["email_invalid"])
        
        return email
        