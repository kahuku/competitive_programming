import random

a = random.sample(range(1,20),random.randint(5,10))
b = random.sample(range(1,20),random.randint(5,10))

c = [elem for elem in a if elem in b]

print (c)
