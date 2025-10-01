#20251001
#9375 패션왕 신해빈
#dict 활용

import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    a = {}
    for _ in range(n):
        name, type=input().split()
        a[type]=a.get(type,0)+1
        #print(a)
    result=1
    for i in a.values():
        result*=(i+1)
    print(result-1)
