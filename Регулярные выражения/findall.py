import re
line = input()
print(len(re.findall(r'(?=(>>-->))|(?=(<--<<))', line)))