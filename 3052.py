#20251004
#3052 나머지

import sys
input=sys.stdin.readline

a=set()
for _ in range(10):
    a.add(int(input())%42)
print(len(a))

