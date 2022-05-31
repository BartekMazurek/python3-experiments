initial_value = 0
required_value = 100

while initial_value < required_value:
    input_value = int(input('Enter value: '))
    initial_value = initial_value + input_value
    print('Entered value: ', input_value, ', summary: ', initial_value, ', required: ', required_value)

print('Finished, ', initial_value)
