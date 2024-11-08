from colorama import Fore

MENU = f"""{Fore.RESET}
Commands menu:

#1 -{Fore.LIGHTBLACK_EX} hello {Fore.RESET} Say hello to the Bot
#2 -{Fore.BLUE} add <name> <phone> {Fore.RESET} Add new contact
#3 -{Fore.GREEN} change <name> <phone to change> <new phone> {Fore.RESET} Change contact
#4 -{Fore.YELLOW} phone <name> {Fore.RESET} Show phone of the contact
#5 -{Fore.BLUE} add-birthday <name> <birthday date> {Fore.RESET} Add birthday, format DD.MM.YYYY
#6 -{Fore.YELLOW} show-birthday <name> {Fore.RESET} Show birthday of the contact
#7 -{Fore.WHITE} birthdays {Fore.RESET} Show upcoming birthday for 7 days
#8 -{Fore.WHITE} all {Fore.RESET} Show all contacts
#9 -{Fore.RED} close {Fore.RESET}/{Fore.RED} exit {Fore.RESET} Exit the Bot
#10 -{Fore.YELLOW} add-note <name> <description> {Fore.RESET} Add the note
#11 -{Fore.GREEN} show-notes {Fore.RESET} Show all notes
#12 -{Fore.LIGHTBLUE_EX} show-note <name> {Fore.RESET} Show all notes for the contact
#13 -{Fore.BLUE} delete-note <id> {Fore.RESET} Delete note with id
#14 -{Fore.MAGENTA} edit-note <id> <new description> {Fore.RESET} Edit note with id
"""

ERROR_MESSAGES = {
    "phone_and_number_missing": f"{Fore.RED}Give me name and phone please.",
    "name_and_birthday_missing": f"{Fore.RED}Give me name and birthday please.",
    "phone_missing": f"{Fore.RED}Give me phones.",
    "phone_only_num": f"{Fore.RED}The phone number must contain only numbers.",
    "phone_length": f"{Fore.RED}The phone number must contain 10 characters.",
    "phone_already_exists": f"{Fore.RED}This phone already exist.",
    "no_command": f"{Fore.RED}Please enter a command.",
    "no_contact": f"{Fore.RED}No contact found.",
    "no_phone": f"{Fore.RED}Phone not found.",
    "invalid_command": f"{Fore.RED}Invalid command!",
    "invalid_date_format": f"{Fore.RED}Invalid date format. Use DD.MM.YYYY",
    "record_not_found": f"{Fore.RED}The Record with this name not found.",
    "no-notes": f"{Fore.RED}No notes found",
}

MESSAGES = {
    "welcome": f"{Fore.CYAN}Welcome to the assistant bot!",
    "enter_command": f"{Fore.CYAN}Enter a command: {Fore.RESET}",
    "help_question": f"{Fore.GREEN}How can I help you?",
    "contact_added": f"{Fore.GREEN}Contact added.",
    "contact_updated": f"{Fore.GREEN}Contact updated.",
    "contacts_empty": f"{Fore.GREEN}There are no contacts exists.",
    "no_phone_exists": f"{Fore.GREEN}No phone exists.",
    "birthday_added": f"{Fore.GREEN}Birthday added.",
    "no_birthday": f"{Fore.GREEN}No data",
    "upcoming_birthdays_empty": f"{Fore.GREEN}There are no upcoming birthdays",
    "bye": f"{Fore.GREEN}Good bye!",
    "note_updated": f"{Fore.GREEN}Note added.",
    "note_added": f"{Fore.GREEN}Note updated.",
    "notes_empty": f"{Fore.GREEN}There are no notes exists.",
    "no_user_with_this_name": f"{Fore.GREEN}No user found.",
    "note_is_updates": f"{Fore.GREEN}Note is updated",
    "note_deleted": f"{Fore.GREEN}Note is deleted",
}
