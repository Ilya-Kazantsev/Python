# 45 88 46 84 531 44
# I способ
# map применяет функцию int ко всем элементам строкового массива
nums = list(map(int, input().split()))

# II способ
nums = []
values = input().split()
for i in values:
    nums.append(int(values[i]))

print(nums)

