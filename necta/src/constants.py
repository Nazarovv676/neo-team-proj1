from colorama import Fore

MENU = f"""{Fore.RESET}
Commands menu:

#1 -{Fore.LIGHTBLACK_EX} hello {Fore.RESET} Say hello to the Bot

{Fore.CYAN}---Contacts---{Fore.RESET}
#2 -{Fore.BLUE} add <name> <phone> {Fore.RESET} Add new contact
#3 -{Fore.BLUE} add-phone <name> <phone> {Fore.RESET} Add phone to contact
#4 -{Fore.GREEN} change <name> <phone to change> <new phone> {Fore.RESET} Change contact
#5 -{Fore.YELLOW} phone <name> {Fore.RESET} Show phone of the contact
#6 -{Fore.BLUE} add-birthday <name> <birthday date> {Fore.RESET} Add birthday, format DD.MM.YYYY
#7 -{Fore.YELLOW} show-birthday <name> {Fore.RESET} Show birthday of the contact
#8 -{Fore.WHITE} birthdays <days> {Fore.RESET} Show upcoming birthday for given days (default 7)
#9 -{Fore.BLUE} add-address <name> <address> {Fore.RESET} Add address
#10 -{Fore.BLUE} add-email <name> <email> {Fore.RESET} Add email
#11 -{Fore.RED} delete-contact <name> {Fore.RESET} Delete contact
#12 -{Fore.WHITE} all {Fore.RESET} Show all contacts

{Fore.CYAN}---Notes---{Fore.RESET}
#13 -{Fore.RED} add-note <name> <description> {Fore.RESET} Add the note
#14 -{Fore.LIGHTRED_EX} show-notes {Fore.RESET} Show all notes
#15 -{Fore.YELLOW} show-note <name> {Fore.RESET} Show all notes for the contact
#16 -{Fore.GREEN} delete-note <name> {Fore.RESET} Delete note with id
#17 -{Fore.LIGHTBLUE_EX} edit-note <name> <new description> {Fore.RESET} Edit note with id
#18 -{Fore.BLUE} add-note-tag <name> <tag> {Fore.RESET} Add tag to the note
#19 -{Fore.MAGENTA} find-notes-by-tag <tag> {Fore.RESET} Find notes by a special tag

#20 -{Fore.RED} close {Fore.RESET}/{Fore.RED} exit {Fore.RESET} Exit the Bot
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
    "email_invalid": f"{Fore.RED}The email should be in the format example@domain.com.",
    "name_and_address_missing": f"{Fore.RED}Give me name and address please.",
    "name_and_email_missing": f"{Fore.RED}Give me name and email please.",
    "name_missing": f"{Fore.RED}Give me name please.",
    "name_and_phone_missing": f"{Fore.RED}Give me name and phone please.",
    "invalid_input_id_value": f"{Fore.RED}Id must be an integer.",
    "no-tags": f"{Fore.RED}This tag exists!",
    "notes-input-exception": f"{Fore.RED}Name and tag are required!",
}

MESSAGES = {
    "welcome": f"{Fore.CYAN}Welcome to the assistant bot!",
    "help_question": f"{Fore.GREEN}How can I help you?",
    "contact_added": f"{Fore.GREEN}Contact added.",
    "phone_added": f"{Fore.GREEN}New phone added to contact.",
    "contact_updated": f"{Fore.GREEN}Contact updated.",
    "contact_deleted": f"{Fore.GREEN}Contact deleted.",
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
    "email_added": f"{Fore.GREEN}Email added.",
    "address_added": f"{Fore.GREEN}Address added.",
    "tag_is_added": f"{Fore.GREEN}Tag is added.",
    "clarify_contact": f"{Fore.BLUE}What contact do you mean?{Fore.RESET}",
    "enter_contact_id": f"{Fore.GREEN}Enter the appropriate contact number or {Fore.RED}cancel{Fore.RESET}:",
}
