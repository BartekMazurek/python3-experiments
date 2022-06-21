# FUNCTIONS PERFORMANCE MEASURE
import time


def sum_into_value(number_argument):
    result = 0

    for number in range(1, number_argument + 1):
        result = result + number

    return result


def sum_into_value2(number_argument):
    return sum(number for number in range(1, number_argument + 1))


def sum_into_value3(number_argument):
    return (1 + number_argument) / 2 * number_argument


value_to_check = 100000000

# MEASURE FIRST FUNCTION PERFORMANCE
start = time.perf_counter()
sum_into_value(value_to_check)
end = time.perf_counter()
print('First function performance: ', end - start)

# MEASURE SECOND FUNCTION PERFORMANCE
start = time.perf_counter()
sum_into_value2(value_to_check)
end = time.perf_counter()
print('Second function performance: ', end - start)

# MEASURE THIRD FUNCTION PERFORMANCE
start = time.perf_counter()
sum_into_value3(value_to_check)
end = time.perf_counter()
print('Third function performance: ', end - start)
