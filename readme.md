# Contacts and Notes Bot

This is a bot for saving, changing, and reviewing phone contacts and notes. The bot supports various commands to manage contacts and notes efficiently.

## Features

- Add, change, and show contacts
- Add, show, and delete notes
- Add birthdays, addresses, and emails to contacts
- Show upcoming birthdays

## Requirements

- Python 3.10 or higher
- Required packages listed in `requirements.txt`

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment:
    ```sh
    python -m venv .env
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        .env\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source .env/bin/activate
        ```

4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the bot:
    ```sh
    python main.py
    ```

2. Enter commands to interact with the bot. The available commands are:

    - `hello`: Say hello to the Bot
    - `add <name> <phone>`: Add a new contact
    - `change <name> <phone to change> <new phone>`: Change a contact's phone number
    - `phone <name>`: Show the phone number of a contact
    - `add-birthday <name> <birthday date>`: Add a birthday (format: DD.MM.YYYY)
    - `show-birthday <name>`: Show the birthday of a contact
    - `birthdays <name>`: Show upcoming birthdays for the next given days
    - `add-address <name> <address>`: Add an address to a contact
    - `add-email <name> <email>`: Add an email to a contact
    - `all`: Show all contacts
    - `add-note <name> <description>`: Add a note
    - `show-notes`: Show all notes
    - `show-note <name>`: Show all notes for a contact
    - `delete-note <id>`: Delete a note by ID
    - `edit-note <id> <new description>`: Edit a note by ID
    - `close` or `exit`: Exit the Bot

## Example

```sh
$ python main.py
Welcome to the assistant bot!

Commands menu:

#1 - hello  Say hello to the Bot
#2 - add <name> <phone>  Add new contact
#3 - change <name> <phone to change> <new phone>  Change contact
#4 - phone <name>  Show phone of the contact
#5 - add-birthday <name> <birthday date>  Add birthday, format DD.MM.YYYY
#6 - show-birthday <name>  Show birthday of the contact
#7 - birthdays <days>  Show upcoming birthday for given days (default 7)
#8 - add-address <name> <address>  Add address
#9 - add-email <name> <email>  Add email
#10 - all  Show all contacts
#11 - add-note <name> <description>  Add the note
#12 - show-notes  Show all notes
#13 - show-note <name>  Show all notes for the contact
#14 - delete-note <id>  Delete note with id
#15 - edit-note <id> <new description>  Edit note with id

#16 - close / exit  Exit the Bot

Enter a command: add John 1234567890
Contact added.

Enter a command: phone John
1234567890