#20250729
#1456 거의 소수
#정수론-에라토스테네스의 체

import math

Min, Max = map(int, input().split())
a = [0] * 10000001


for i in range(2, len(a)):
    a[i] = i

#에라토스테네스의 체
for i in range(2, int(math.sqrt(len(a))) + 1):
    if a[i] == 0:
        continue
    for j in range(i * 2, len(a), i):
        a[j] = 0

count = 0

for i in range(2, 10000001):
    if a[i] != 0:
        tmp = a[i] * a[i]
        while tmp <= Max:
            if tmp >= Min:
                count += 1

            if tmp > Max // a[i]:
                break
            tmp *= a[i]

print(count)
