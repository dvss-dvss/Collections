from random import randint

n = int(input('Кількість елементів: '))
numbers = [randint(1, 10) for x in range(n)]
print(*numbers)

p = int(input('Елемент для видылення: '))
filtered_numbers = [x for x in numbers if x != p]
print(*filtered_numbers)