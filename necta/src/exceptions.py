from functools import wraps

from colorama import Fore
from .constants import ERROR_MESSAGES


class PhoneException(Exception):
    pass


class BirthdayException(Exception):
    pass


class EmailException(Exception):
    pass


class AddressException(Exception):
    pass


class NameException(Exception):
    pass

class RecordNotFound(Exception):
    pass


class InvalidCommand(Exception):
    pass


class NoContactFound(Exception):
    pass


class NoNotesFound(Exception):
    pass

class TagException(Exception):
    pass

class NotesInputException(Exception):
    pass


class NoteException(Exception):
    pass


class SearchException(Exception):
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
        except NotesInputException as e:
            return  f"{Fore.RED}{e}"
        except TagException as e:
            return f"{Fore.RED}{e}"
        except PhoneException as e:
            return e
        except BirthdayException as e:
            return e
        except RecordNotFound:
            return ERROR_MESSAGES["record_not_found"]
        except EmailException as e:
            return e
        except AddressException as e:
            return e
        except NameException as e:
            return e
        except NoteException as e:
            return e
        except SearchException as e:
            return e
            

    return inner
