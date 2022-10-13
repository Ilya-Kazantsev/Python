mas = list(map(int, input().split()))
mas1 = list(map(int, input().split()))
print(mas[:mas1[0]:], mas[mas1[0]:mas1[1]:-1], mas[mas1[1] + 1::])
print(mas[1:4:-1])