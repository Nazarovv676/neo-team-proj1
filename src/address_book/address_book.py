from collections import UserDict
from src import RecordNotFound, ERROR_MESSAGES
from src.address_book import Record
from datetime import datetime, timedelta


class AddressBook(UserDict):
    """
    Class for the Address Book that stores and manages all records
    """

    records = 0

    def add_record(self, record: Record):
        self.data[record] = AddressBook.records
        AddressBook.records += 1

    def find(self, name: str):
        for record in self.data.keys():
            record_name = record.name.value
            if record_name == name:
                return record
        return None

    def delete(self, name: str):
        records = list(
            filter(lambda record: record.name.value == name, self.data.keys())
        )
        if not len(records):
            raise RecordNotFound(ERROR_MESSAGES["invalid_date_format"])
        self.data.pop(records[0])
        AddressBook.records -= 1

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        in_7_days_date = today + timedelta(days=10)

        upcoming_birthdays = []
        for record in self.data.keys():
            if not record.birthday:
                continue
            birthday = record.birthday.value.date()

            congratulation_date = datetime(
                year=today.year, month=birthday.month, day=birthday.day
            ).date()
            if (today.month, today.day) > (birthday.month, birthday.day):
                congratulation_date = datetime(
                    year=today.year + 1, month=birthday.month, day=birthday.day
                ).date()

            if today <= congratulation_date <= in_7_days_date:
                birthdays_weekday = congratulation_date.isocalendar()[2]

                if birthdays_weekday == 6:
                    congratulation_date = congratulation_date + timedelta(days=2)

                if birthdays_weekday == 7:
                    congratulation_date = congratulation_date + timedelta(days=1)

                upcoming_birthdays.append(
                    {
                        "name": record.name.value,
                        "congratulation_date": congratulation_date.strftime("%d.%m.%Y"),
                    }
                )

        return upcoming_birthdays
