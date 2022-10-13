n = int(input())
matrix = [[0 for i in range(3)] for j in range(n)]
for i in range(n):
    line = input()
    for j in range(len(line)):
        matrix[i][j] = line[j]

sum = 0
def Check(matrix, j, i):
    global sum
    if i < len(matrix) - 1:
        if matrix[i + 1][j] != 'W':
            if matrix[i + 1][j] == 'C':
                sum += 1
            Check(matrix, j, i + 1)
        if j < 2 and matrix[i + 1][j + 1] != 'W':
            if matrix[i + 1][j + 1] == 'C':
                sum += 1
            Check(matrix, j + 1, i + 1)
        if j > 0 and matrix[i + 1][j - 1] != 'W':
            if matrix[i + 1][j - 1] == 'C':
                sum += 1
            Check(matrix, j - 1, i + 1)


Check(matrix, 1, 0)
print(sum)
