import re
n = int(input())
ans = ''
for i in range(n):
    number = input()
    if len(number) != 6:
        ans += 'No\n'
    elif re.match(r'[ABCEHKMOPTXY]\d{3}[ABCEHKMOPTXY]{2}', number):
        ans += 'Yes\n'
    else:
        ans += 'No\n'
print(ans)
