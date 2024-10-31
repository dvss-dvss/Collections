from random import randint
from faker import Faker

fake = Faker()

n = int(input('Кількість учнів: '))
MARKS_COUNT = 3

pupils = {fake.name(): [randint(4, 12) for _ in range(MARKS_COUNT)] for _ in range(n)}
print(pupils)

average_scores = {name: round(sum(marks) / MARKS_COUNT, 2) for name, marks in pupils.items()}

sorted_pupils = sorted(pupils.items(), key=lambda x: (-average_scores[x[0]], x[0]))

for name, marks in sorted_pupils:
    marks_str = ' '.join(str(mark) for mark in marks)
    average_score = average_scores[name]
    print(f"{name:<30} {marks_str} --> {average_score:.2f}")
