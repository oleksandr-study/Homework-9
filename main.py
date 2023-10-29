phone_base = {}


def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Not enough parametrs. Please, enter Command, Name and Phone number"
        except KeyError:
            return "Wrong Name. Please enter correct Name"
    return inner

@input_error
def hello():
    return "How I can help you?"

@input_error
def add_record(*args):
    user_name = args[0]
    phone_number = args[1]
    phone_base[user_name] = phone_number
    return f"Added user: {user_name} with phone number: {phone_number}"

@input_error
def change_record(*args):
    user_name = args[0]
    new_phone_number = args[1]
    new_record = phone_base[user_name]
    if new_record:
        phone_base[user_name] = new_phone_number
        return f"Users {user_name} phone changed to {new_phone_number}"

@input_error
def show_phone(*args):
    user_name = args[0]
    return f"{user_name} phone number {phone_base[user_name]}"

@input_error
def show_all(*args):
    return phone_base

@input_error
def good_bye(*args):
    return "\nGood bye." 

COMMANDS = {hello: "hello",
            add_record: "add",
            change_record: "change",
            show_phone: "phone",
            show_all: "show all",
            good_bye: ("good bye", "close")}

def unknown_command(*args):
    return "Unknown command. Please try again."

def parser(text: str):
    for func, kw in COMMANDS.items():
        register_text = text.lower()
        if register_text.startswith(kw):
            return func, text[len(kw):].strip().split()
    return unknown_command, []
    
def main():
    while True:
        input_command = input("Please input command: ")
        func, data = parser(input_command)
        print(func(*data))
        if func(*data) == "\nGood bye.":
            break

if __name__ == "__main__":
    main()