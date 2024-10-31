from random import randint
from faker import Faker

fake = Faker()

n = int(input('Килькисть учнів: '))
MARKS_COUNT = 3

pupils = {fake.name(): [randint(4, 12) for _ in range(MARKS_COUNT)] for _ in range(n)}
print(pupils)

for name in pupils:
    marks = ' '.join(str(mark) for mark in pupils[name])
    print(f"{name:<30} {marks}")

avg_marks = [sum(pupils[name][i] for name in pupils) / n for i in range(MARKS_COUNT)]
print((" " * 31) + " ".join(f"{mark:>5.2f}" for mark in avg_marks))