#20251007
#10816 숫자 카드 2

import sys
input=sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

OFFSET = 10_000_000
SIZE = 20_000_001
freq = [0] * SIZE

for x in a:
    freq[x + OFFSET] += 1

out = []
for x in b:
    out.append(freq[x + OFFSET])

print(*out)
