# FUNCTION AS FUNCTION ARGUMENT

def show_message(message_content):
    print('Some random message content: ', message_content)


def execute_function_with_argument(func, argument):
    func(argument)


execute_function_with_argument(show_message, 'content')
