# DEFINED NESTED DATA TYPES

try:

    definitions = {

    }

    while True:
        print('1: Add definition')
        print('2: Find definition')
        print('3: Delete definition')
        print('4: Exit')

        operationValue = int(input('Choose operation: '))

        if operationValue == 1:
            keyName = input('Enter key name: ')
            definition = input('Enter key value definition: ')
            definitions[keyName] = definition
            print('Added new definition')

        elif operationValue == 2:
            keyToFind = input('Enter key name to find: ')

            if keyToFind in definitions:
                print(definitions[keyToFind])
            else:
                print('Specified key does not exist in definitions')

        elif operationValue == 3:
            keyToDelete = input('Enter key name to delete: ')

            if keyToDelete in definitions:
                del definitions[keyToDelete]
            else:
                print('Specified key does not exist in definitions')

        elif operationValue == 4:
            print('Exited')

            break

        else:
            print('Wrong operation number. Exited')

            break
except ValueError:
    print("Wrong command number. Exited")
