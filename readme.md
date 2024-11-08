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
    - `menu`: Show the menu
    - `add <name> <phone>`: Add a new contact
    - `change <name> <phone to change> <new phone>`: Change a contact's phone number
    - `phone <name>`: Show the phone number of a contact
    - `add-birthday <name> <birthday date>`: Add a birthday (format: DD.MM.YYYY)
    - `show-birthday <name>`: Show the birthday of a contact
    - `birthdays <days>`: Show upcoming birthdays for the next given days
    - `add-address <name> <address>`: Add an address to a contact
    - `add-email <name> <email>`: Add an email to a contact
    - `all`: Show all contacts
    - `add-note <name> <description>`: Add a note
    - `show-notes`: Show all notes
    - `show-note <name>`: Show all notes for a contact
    - `delete-note <id>`: Delete a note by ID
    - `edit-note <id> <new description>`: Edit a note by ID
    - `delete-contact <name>`: Delete a contact by name
    - `close` or `exit`: Exit the Bot
