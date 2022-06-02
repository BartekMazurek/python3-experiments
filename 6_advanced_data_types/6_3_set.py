# SET
# HAS VALUES ONLY

test_set = {5, 6, 10, 10, 1, 3, 2}
print("Test set: ", test_set)

# ADD NEW ELEMENT
test_set.add(9)
print("Set with added new element: ", test_set)

# CONVERT LIST INTO SET WITH UNIQUE SORTED ELEMENTS
test_list = [1, 1, 1, 2, 2, 2, 3, 4, 5]
second_test_set = set(test_list)

print("Converted list into set: ", second_test_set)

# COMPARE TWO SETS AND GET COMMON ELEMENTS
third_test_set = {1, 2, 3, 4}
fourth_test_set = {3, 4, 5, 6}
print("Two sets common elements: ", third_test_set & fourth_test_set)

print("Compared sets: ", third_test_set - fourth_test_set)

# XOR - GET TWO SETS NOT COMMON ELEMENTS
print("XOR on two sets: ", third_test_set ^ fourth_test_set)

# CHECK IF SET IS SUBSET OF SECOND SET
print(third_test_set.issubset(fourth_test_set))
