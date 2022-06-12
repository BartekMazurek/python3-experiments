# LIST TRANSFORMATION

numbers = [1, 2, 3, 4, 5, 6]
powered_numbers = []

# NON EFFICIENT WAY TO TRANSFORM LIST DATA
for number in numbers:
    powered_numbers.append(number**2)

print('Powered numbers: ', powered_numbers)

# LIST TRANSFORMATION EXPRESSION
# [ELEMENT/OPERATION - ELEMENT - ELEMENTS COLLECTION - CONDITION]
# [
#     WHAT TO DO ON ELEMENT
#     FOR ELEMENT IN ELEMENTS
#     CONDITION BASED ON ELEMENT
# ]

alternative_powered_numbers = [number ** 2 for number in numbers]
print('Alternative powered numbers: ', alternative_powered_numbers)

even_numbers = [
    number for number in alternative_powered_numbers
    if (number % 2 == 0)
]
print('Even powered numbers: ', even_numbers)
