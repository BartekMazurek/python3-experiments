# LIST GENERATORS

import sys

# NOT EFFICIENT WAY TO GENERATE ELEMENTS
# BIG AMOUNT OF RAM ALLOCATED IMMEDIATELY FOR ALL ELEMENTS ON LIST
even_numbers = [
    element
    for element in range(5000)
    if (element % 2 == 0)
]

even_numbers_size = sys.getsizeof(even_numbers)
print('Even numbers size: ', even_numbers_size)

# MORE EFFICIENT WAY TO GENERATE ELEMENTS
# RETURN GENERATOR OBJECT TO RETRIEVE ELEMENTS
# RECOMMENDED WAY TO PROCESS BIG AMOUNT OF DATA (FOR EXAMPLE TEXT/EXCEL FILE)
# SHOULD BE USED IF ACCESS INTO ELEMENTS AFTER PROCESSING IT IS NOT REQUIRED
even_numbers_generator = (
    element
    for element in range(5000)
    if (element % 2 == 0)
)

even_numbers_generator_size = sys.getsizeof(even_numbers_generator)
print('Even numbers generator size: ', even_numbers_generator_size)

# PRINT GENERATOR ELEMENTS
# for element in even_numbers_generator:
#     print(element)
