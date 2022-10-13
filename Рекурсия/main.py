'''
Рекурсия
Для рекурсии важно указать признак окончании рекурсии.
У рекурсии есть прямой и обратный ход.
'''

def printSeq(n):
    if n > 0:
        printSeq(n - 1)
        print(n, end=' ')

def sumSeq(n):
    if n > 0:
        return sumSeq(n - 1) + n
    return 0

print(sumSeq(10))