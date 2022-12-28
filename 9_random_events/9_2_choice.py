# CHOICE
import random
from collections import Counter

# FIRST EXAMPLE - choice
musician_list = ["Michael Jackson", "Robbie Williams", "Lenny Kravitz"]
print('Random picked musician: ', random.choice(musician_list))

# SECOND EXAMPLE - choices
# MORE ADVANCED THAN CHOICE
# ALLOWED TO SET POSSIBILITY OF SPECIFIED CHOICE ELEMENT
# weights - WEIGHT AVERAGE - SPECIFY WEIGHTS OF RANDOMLY PICKED UP ELEMENTS
# k - AMOUNT OF RANDOM ATTEMPTS
actors_list = ["Monica Bellucci", "Penelope Cruz", "Leslie Bega"]
print('More randomly picked actors with specified weights: ')
counted_actors = Counter(random.choices(actors_list, weights=[1, 2, 1], k=100))
print(counted_actors)

# THIRD EXAMPLE - SET PERCENT PROBABILITY TO PICKUP ELEMENT FROM LIST
counted_again_actors = Counter(random.choices(actors_list, weights=[80, 15, 5], k=10000))
print(counted_again_actors)
