# COMPARE OPERATORS

# 1
# firstValue = int(input('Enter first value: '))
# secondValue = int(input('Enter second value: '))
firstValue = 1
secondValue = 2

if firstValue > secondValue:
    print('First value greater than second one')
    print('First condition')
elif firstValue == secondValue:
    print('Values are equal')
    print('Second condition')
else:
    print('Second value greater than first one')
    print('Third condition')

print('Checked')

# 2
# thirdValue = False
# thirdValue = 0
thirdValue = True

if thirdValue:
    print('Value is set')

# 3
fourthValue = 4
fifthValue = 4

if (fourthValue % 2 == 0) and (fifthValue % 2 == 0):
    print('Even values')
else:
    print('Odd values')
