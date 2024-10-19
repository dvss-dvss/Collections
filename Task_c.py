from random import randint

n = int(input('Кількість елементів: '))
numbers = [randint(1, 10) for x in range(n)]
print(*numbers)

p = int(input('Номер елементу для видалення: '))
del numbers[p - 1]

q, k = [int(s) for s in input('Номер та значення елемента для вставки через пробіл: ').split()]

numbers.insert(q - 1, k)
print(*numbers)