import module

try:

    operation = int(input('Choose operation number: '))
    first_argument = int(input('Set first argument value: '))
    second_argument = int(input('Set second argument value: '))

    result = 0

    if operation == module.available_operations.multiply:
        result = module.multiply(first_argument, second_argument)

    elif operation == module.available_operations.divide:
        result = module.divide(first_argument, second_argument)

    elif operation == module.available_operations.add:
        result = module.add(first_argument, second_argument)

    elif operation == module.available_operations.subtract:
        result = module.subtract(first_argument, second_argument)
    else:
        print('Method not implemented')

    print('Result: ', result)

except ValueError:
    print("Wrong command number. Exited")
