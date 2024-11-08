from functools import wraps
from src.constants import ERROR_MESSAGES


class PhoneException(Exception):
    pass


class BirthdayException(Exception):
    pass


class EmailException(Exception):
    pass


class AddressException(Exception):
    pass

class RecordNotFound(Exception):
    pass


class InvalidCommand(Exception):
    pass


class NoContactFound(Exception):
    pass


class NoNotesFound(Exception):
    pass


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return ERROR_MESSAGES["phone_and_number_missing"]
        except IndexError:
            return ERROR_MESSAGES["phone_missing"]
        except KeyError:
            return ERROR_MESSAGES["no_contact"]
        except NoContactFound:
            return ERROR_MESSAGES["no_contact"]
        except NoNotesFound:
            return ERROR_MESSAGES["no-notes"]
        except PhoneException as e:
            return e
        except BirthdayException as e:
            return e
        except RecordNotFound as e:
            return e
        except EmailException as e:
            return e
        except AddressException as e:
            return e
            

    return inner
