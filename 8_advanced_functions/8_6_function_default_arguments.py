# FUNCTION DEFAULT ARGUMENTS

def test_function(first_argument=1, second_argument=10, third_argument=2):
    result = 0

    for value in range(first_argument, second_argument + 1):
        result = result + third_argument

    return result


result_value = test_function(1, 10, 100)
print('Result value: ', result_value)
