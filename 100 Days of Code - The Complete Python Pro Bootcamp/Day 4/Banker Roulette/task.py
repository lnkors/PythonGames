friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

import random

#1 Option - Using this function to pick random item from a data structure list
print(random.choice(friends))

#Option #2 - Using random int to get this
index = random.randint(0,4)
print(friends[index])
