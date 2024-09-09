import sys

def check_args(args, expected_args_num):
    if len(args) < expected_args_num:
        return f"Please provide {expected_args_num} arguments.", False
    elif len(args) > expected_args_num:
        return f"Too many count of arguments, expected {expected_args_num}", False
    else:
        return "", True

def parse_input(user_input):
    cmd, *args = user_input.split() 
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args

    if name in contacts:
        return f"Contact {name} already exists!"
    
    contacts[name] = phone
    
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args

    if name in contacts:
        contacts[name] = phone
    else:
        return f"Contact with username {name} does not exists!"

    return "Contact updated."

def show_all(contacts):
    return contacts

def show_phone(args, contacts):    
    username = args[0]
    if username in contacts:
        return contacts[username]
    else:
        return f"Contact {username} does not exists!"

def main():
    contacts = {}
    print("Welcome to the assistent bot!")

    while True:
        user_input = input("Enter a command:")
        command, *args = parse_input(user_input)
        
        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            error_message, valid = check_args(args, 2)
            if valid:
                print(add_contact(args, contacts))
            else:
                print(error_message)
        elif command == 'all':
            print(show_all(contacts))
        elif command == "change":
            error_message, valid = check_args(args, 2)
            if valid:
                print(change_contact(args, contacts))
            else:
                print(error_message)
        elif command == 'phone':
            error_message, valid = check_args(args, 1)
            if valid:
                print(show_phone(args, contacts))
            else:
                print(error_message)
        else:
            print("Invalid command!")

if __name__ == "__main__":
    main()