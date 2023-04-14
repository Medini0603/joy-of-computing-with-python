import random

i=random.randint(1,5)
# geneartes 1,2,3,4,5 
print(i)

i=random.randrange(1,5)
# generates 1,2,3,4
print(i)

i=random.random()
# generates decimal numbers from 0 to 1
print(i)

i=random.randrange(1,10,2)
# generates odd numbers from 1 to 10
print(i)

i=random.randrange(2,11,2)
# generates even numbers from 2 to 10
print(i)

i=random.choice([3,14,13,25])
# generates number from given list 
print(i)

list=[4,14,15,26]
i=random.choice(list)
# generates number from given list 
print(i)