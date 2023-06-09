import random

# print(random.random())
# print(random.randint(1,10))
# print(random.randrange(1,10,2))

# print(random.choice("Computer"))

l= [12,34,45,25,67,43,59]
m = random.randint(0,7)
print(l[m])
random.shuffle(l)
print(l)