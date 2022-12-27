# ANONYMOUS/LAMBDA FUNCTIONS
# USE lambda TO CREATE FUNCTION
# STRUCTURE: lambda argument: logic with argument, argument_value

test_list = [2, 10, 1, 5, 4, 99, 0]

# FIRST EXAMPLE
filtered_list = list(filter(lambda x: x % 2 == 0, test_list))
print('Filtered list: ', filtered_list)

# SECOND EXAMPLE - MORE SELF-DESCRIPTIVE
second_filtered_list = [element for element in test_list if (element % 2) == 0]
print('Second filtered list :', second_filtered_list)
