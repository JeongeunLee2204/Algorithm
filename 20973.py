#20250818
#20973 Uddered but not Herd
#문자열 구현

import sys
input=sys.stdin.readline

cow = input().strip()
x = input().strip()

count = 1
i = 0

for ch in x:
    pos = cow.find(ch, i)
    if pos == -1:
        count += 1
        i = cow.find(ch) + 1
    else:
        i = pos + 1

print(count)
