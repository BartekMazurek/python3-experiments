# MULTIPLE UNKNOWN ARGUMENTS

def multiple_arguments(*arg):

    print(type(arg))

    for argument in arg:
        print('Type: ', type(argument), ' value: ', argument)


multiple_arguments(1, 2, "3", "Test")
