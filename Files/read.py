try:
    fInput = open('input1.txt')
    fInput.close()
except FileNotFoundError as e:
    print(f'Файл {e.filename} не найден!')


# Чтение всего текста из файла
text = fInput.read()
print(text)

# Получение из файла массива строк
lines = fInput.readlines()
print(lines)

# Построчное чтение
for line in fInput:
    print(line.strip())

# Чтобы не закрывать файл, можно пользоваться конструкцией with
with open('input.txt') as fInput:
    for line in fInput:
        print(line.strip())
