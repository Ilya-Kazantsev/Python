import random

# Генератор, заполняющий массив случайными числами
l = [random.randint(1, 100) for i in range(10)]

'''
for i in range(10):
    l.append(random.randint(1, 100))
'''

# Вывод массива на экран
# I способ
for i in range(len(l)):
    print(l[i], end=' ')

# II способ
for i in l:
    print(i, end=' ')