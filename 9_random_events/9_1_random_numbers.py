# RANDOM NUMBERS

import random

# RANDOM NUMBER (FLOAT) FROM RANGE -3.5 <= x < 5.5
first = random.uniform(-3.5, 5.5)
print('First: ', first)

# RANDOM NUMBER (INT) FROM RANGE 0, 1 ... 10
second = random.randrange(0, 10)
print('Second: ', second)

# RANDOM EVEN NUMBER (INT) FROM RANGE 0, 2, 4 ... 10
third = random.randrange(0, 10, 2)
print('Third: ', third)
