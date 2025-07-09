# 20250709
# 10989 수 정렬하기 3
# 계수 정렬

import sys
input = sys.stdin.readline

n = int(input())
count = [0] * 10001

for _ in range(n):
    a = int(input())
    count[a] += 1

for i in range(10001):
    for _ in range(count[i]):
        print(i)
