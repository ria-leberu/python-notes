from random import random, sample

LIST_SIZE = 20
MAX_VALUE = 20

random_list = sample(range(MAX_VALUE), LIST_SIZE)


print(random_list)

print(sorted(random_list))
