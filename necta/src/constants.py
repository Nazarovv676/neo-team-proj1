from colorama import Fore

MENU = f"""{Fore.RESET}
Commands menu:

#1 -{Fore.LIGHTBLACK_EX} hello {Fore.RESET} Say hello to the Bot
#2 -{Fore.LIGHTBLACK_EX} menu {Fore.RESET} Show the menu
#3 -{Fore.LIGHTBLACK_EX} search <query> {Fore.RESET} Search for contacts and notes
#4 -{Fore.RED} close {Fore.RESET}/{Fore.RED} exit {Fore.RESET} Exit the Bot

{Fore.CYAN}---Contacts---{Fore.RESET}
#5 -{Fore.GREEN} add <name> <phone> {Fore.RESET} Add new contact
#6 -{Fore.GREEN} add-phone <name> <phone> {Fore.RESET} Add phone to contact
#7 -{Fore.YELLOW} change <name> <phone to change> <new phone> {Fore.RESET} Change contact
#8 -{Fore.WHITE} phone <name> {Fore.RESET} Show phone of the contact
#9 -{Fore.GREEN} add-birthday <name> <birthday date> {Fore.RESET} Add birthday, format DD.MM.YYYY
#10 -{Fore.WHITE} show-birthday <name> {Fore.RESET} Show birthday of the contact
#11 -{Fore.WHITE} birthdays <days> {Fore.RESET} Show upcoming birthday for given days (default 7)
#12 -{Fore.GREEN} add-address <name> <address> {Fore.RESET} Add address
#13 -{Fore.GREEN} add-email <name> <email> {Fore.RESET} Add email
#14 -{Fore.RED} delete-contact <name> {Fore.RESET} Delete contact
#15 -{Fore.WHITE} all {Fore.RESET} Show all contacts

{Fore.CYAN}---Notes---{Fore.RESET}
#16 -{Fore.GREEN} add-note <name> <description> {Fore.RESET} Add the note
#17 -{Fore.WHITE} show-notes {Fore.RESET} Show all notes
#18 -{Fore.WHITE} show-note <name> {Fore.RESET} Show all notes for the contact
#19 -{Fore.RED} delete-note <name> {Fore.RESET} Delete note with name
#20 -{Fore.YELLOW} edit-note <name> <new description> {Fore.RESET} Edit note with name
#21 -{Fore.BLUE} add-note-tag <name> <tag> {Fore.RESET} Add tag to the note
#22 -{Fore.YELLOW} find-notes-by-tag <tag> {Fore.RESET} Find notes by a special tag
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
    "note_not_found": f"{Fore.RED}Note not found.",
    "search_query_missing": f"{Fore.RED}Give me a query to search.",
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
