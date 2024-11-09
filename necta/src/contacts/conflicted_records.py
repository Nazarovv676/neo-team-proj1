from necta.src.constants import MESSAGES, ERROR_MESSAGES
from necta.src.contacts import Record
from tabulate import tabulate


def input_record_id(records: list[Record]):
    table_data = [
        (
            user.id.value,
            user.name.value,
            str.join("\n", map(lambda phone: phone.value, user.phones)),
            user.email.value if user.email else "-",
            user.address.value if user.address else "-",
            user.birthday.format_birthday() if user.birthday else "-",
        )
        for user in records
    ]
    try:
        user_input = input(
            f"""
{MESSAGES['clarify_contact']}
{tabulate(table_data, headers=["Number", "Name", "Phones", "Email", "Address", "Birthday"], tablefmt="fancy_grid")}
{MESSAGES['enter_contact_id']} """
        )
        if user_input == "cancel":
            return None

        contact_id = int(user_input)
        return contact_id
    except ValueError:
        print(ERROR_MESSAGES["invalid_input_id_value"])
        return input_record_id(records)


def select_conflicted_record(records: list[Record]) -> Record | None:
    contact_id = input_record_id(records)
    for record in records:
        if record.id.value == contact_id:
            return record
    return None
