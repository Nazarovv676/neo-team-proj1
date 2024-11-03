from src.constants import ERROR_MESSAGES


class PhoneException(Exception):
    pass


class BirthdayException(Exception):
    pass


class RecordNotFound(Exception):
    pass


class InvalidCommand(Exception):
    pass


class NoContactFound(Exception):
    pass


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print(e)
            return ERROR_MESSAGES["phone_and_number_missing"]
        except IndexError:
            return ERROR_MESSAGES["phone_missing"]
        except KeyError:
            return ERROR_MESSAGES["no_contact"]
        except NoContactFound:
            return ERROR_MESSAGES["no_contact"]
        except PhoneException as e:
            return e
        except BirthdayException as e:
            return e
        except RecordNotFound as e:
            return e

    return inner
