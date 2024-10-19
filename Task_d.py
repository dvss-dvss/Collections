from random import randint
from faker import Faker

fake = Faker()

n = int(input('Килькисть унив: '))
MARKS_COUNT = 3

pupils = {fake.name(): [randint(4, 12) for _ in range(MARKS_COUNT)] for _ in range(n)}
print(pupils)

for name in pupils:
    marks = ' '.join(str(mark) for mark in pupils[name])
    print(f"{name} {marks} --> {(sum(pupils[name]) / MARKS_COUNT):.2f}")