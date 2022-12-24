# KEY ARGUMENTS - KEY: VALUE (DEFAULT)

# POSITION ARGUMENTS - CALLING ORDER IS IMPORTANT

def say_hello(firstname, message, separator=" "):
    print('Hello ', firstname, ' ', message, sep=separator)


say_hello('Thomas', 'cheers!')

say_hello(message="cheers!", firstname="Thomas", separator="\n")
