class MyCustomException(Exception):
    def init(self, message="Custom exception is occurred"):
        self.message = message
        super().init(self.message)


phone_book = {}


def stats():
    print(f"Count of users: {len(phone_book)}")

def stats():
    print(f"Count of users: {len(phone_book)}")

def add(name_input, phone_input):
    if name_input in phone_book:
        print(f"The name '{name_input}' already exists.")
    else:
        phone_book[name_input] = phone_input
        print(f"The name '{name_input}' and number '{phone_input}' have been added to the phone book.")

def delete(name_input):
    if name_input in phone_book:
        del phone_book[name_input]
        print(f"Contact '{name_input}' has been deleted.")
    else:
        print(f"Contact '{name_input}' does not exist.")

def list_names():
    print("All contacts from phone book:")
    for name_input in phone_book:
        print(name_input)

def show(name_input):
    if name_input in phone_book:
        print(f"Name: {name_input}, Number: {phone_book[name_input]}")
    else:
        print(f"Contact '{name_input}' does not exist.")


while True:
    try:
        command = input("Function (stats, add, delete, list, show): ")
        if command == "stats":
            stats()
        elif command == "add":
            name_input = input("Input your name: ")
            phone_input = input("Input your number: ")
            add(name_input, phone_input)
        elif command == "delete":
            name_input = input("Input contact name to delete it: ")
            delete(name_input)
        elif command == "list":
            list_names()
        elif command == "show":
            name_input = input("Input name of contact: ")
            show(name_input)
    except Exception as e:
        print(f"An error occurred: {e}")
