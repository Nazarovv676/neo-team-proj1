from collections import UserList
from src import RecordNotFound
from src.address_book import Record
from datetime import datetime, timedelta


class AddressBook(UserList):
    def add_record(self, user: Record):
        """Adds a new user to the address book"""
        self.append(user)

    def update_record(self, user: Record) -> Record:
        """Updates an existing user in the address book"""
        for idx, record in enumerate(self.data):
            if record.name.value == user.name.value:
                self.data[idx] = user
                return user
        raise RecordNotFound()

    def find(self, name: str) -> Record:
        """Retrieves a user by their name."""
        for record in self.data:
            if record.name.value == name:
                return record
        return None

    def find_all(self) -> list[Record]:
        """Retrieves all users in the address book."""
        return self.data

    def add_birthday(self, name: str, birthday: str):
        self.find(name).add_birthday(birthday)

    def get_upcoming_birthdays(self):
        """
        Get a list of upcoming birthdays within the next 7 days, including today.

        This function checks the birthdays of users and adjusts the congratulation date
        to the next working day if the birthday falls on a weekend (Saturday or Sunday).

        Returns:
            list: A list of dictionaries containing the user's name and the corresponding
                congratulation date in 'DD.MM.YYYY' format.
        """
        date_format = "%d.%m.%Y"
        today = datetime.today().date()
        upcoming_birthdays = []

        for user in self.data:
            if user.birthday is None:
                continue

            birthday = user.birthday.value.date()
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            if 0 <= (birthday_this_year - today).days <= 7:
                congratulation_date = birthday_this_year

                if congratulation_date.weekday() == 5:  # Saturday
                    congratulation_date += timedelta(days=2)  # Move to Monday
                elif congratulation_date.weekday() == 6:  # Sunday
                    congratulation_date += timedelta(days=1)  # Move to Monday

                upcoming_birthdays.append(
                    {
                        "name": user.name,
                        "congratulation_date": congratulation_date.strftime(
                            date_format
                        ),
                    }
                )

        return upcoming_birthdays
