# DEFINED NESTED DATA TYPES

try:

    definitions = {}

    while True:
        print("1: Add definition")
        print("2: Find definition")
        print("3: Delete definition")
        print("4: Exit")

        operation_value = int(input("Choose operation: "))

        if operation_value == 1:
            key_name = input("Enter key name: ")
            definition = input("Enter key value definition: ")
            definitions[key_name] = definition
            print("Added new definition")

        elif operation_value == 2:
            key_to_find = input("Enter key name to find: ")

            if key_to_find in definitions:
                print(definitions[key_to_find])
            else:
                print("Specified key does not exist in definitions")

        elif operation_value == 3:
            key_to_delete = input("Enter key name to delete: ")

            if key_to_delete in definitions:
                del definitions[key_to_delete]
            else:
                print("Specified key does not exist in definitions")

        elif operation_value == 4:
            print("Exited")

            break

        else:
            print("Wrong operation number. Exited")

            break
except ValueError:
    print("Wrong command number. Exited")
