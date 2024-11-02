from random import randint
from faker import Faker

fake = Faker()

n = int(input('Кількість учнів: '))
MARKS_COUNT = 3

pupils = [
    [fake.name()] + [randint(4, 12) for _ in range(MARKS_COUNT)] for _ in range(n)
]

for pupil in pupils:
    avg_marks = sum(pupil[1:]) / MARKS_COUNT
    pupil.insert(0, -avg_marks)
pupils.sort()


for pupil in pupils:
    marks = " ".join(str(mark) for mark in pupil[2:])
    print(f"{pupil[1]} {marks} --> {-pupil[0]:.2f}")