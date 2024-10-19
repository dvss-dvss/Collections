from random import randint

n = int(input('Кількість елементів: '))
numbers = [randint(1, 10) for x in range(n)]
print(*numbers)

p = int(input('Номер елементу для перенесення: '))
numbers.insert(0, numbers.pop(p - 1))
print(*numbers)