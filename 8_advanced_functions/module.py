# ENUMS SHOULD BE USED TO INCREASE CODE READABILITY
from enum import IntEnum

available_operations = IntEnum('Module menu', {'multiply': 1, 'divide': 2, 'add': 3, 'subtract': 4})


def multiply(first_argument, second_argument):
    return first_argument * second_argument


def divide(first_argument, second_argument):
    return first_argument / second_argument


def add(first_argument, second_argument):
    return first_argument + second_argument


def subtract(first_argument, second_argument):
    return first_argument - second_argument
