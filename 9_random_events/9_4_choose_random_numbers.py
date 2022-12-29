# FUNCTION TO GET UNIQUE RANDOM NUMBERS
# SAMPLE - FUNCTION TO DETERMINE DATA SET TO CHOOSE UNIQUE ELEMENTS
# ALL RANDOM ELEMENTS FETCHED FROM SAMPLE ARE UNIQUE

import random


def choose_random_numbers(amount, total_amount):
    print(random.sample(range(total_amount), amount))


choose_random_numbers(5, 15)
