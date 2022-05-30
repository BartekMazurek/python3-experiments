# COMPARE OPERATORS

# 1
# first_value = int(input('Enter first value: '))
# second_value = int(input('Enter second value: '))
first_value = 1
second_value = 2

if first_value > second_value:
    print("First value greater than second one")
    print("First condition")
elif first_value == second_value:
    print("Values are equal")
    print("Second condition")
else:
    print("Second value greater than first one")
    print("Third condition")

print("Checked")

# 2
# third_value = False
# third_value = 0
third_value = True

if third_value:
    print("Value is set")

# 3
fourth_value = 4
fifth_value = 4

if (fourth_value % 2 == 0) and (fifth_value % 2 == 0):
    print("Even values")
else:
    print("Odd values")
