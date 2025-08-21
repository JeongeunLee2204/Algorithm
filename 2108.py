#20250821
#2108 통계학

import sys
input=sys.stdin.readline

n=int(input())
a=[int(input()) for _ in range(n)]
a.sort()

def fre(a):
    b=[0]*8001
    for v in a:
        b[v+4000]+=1

    maxc = max(b)
    can = [i-4000 for i,c in enumerate(b) if c==maxc]
    return can[0] if len(can)==1 else can[1]

print(int(round(sum(a)/n,0)))
print(a[n//2])
print(fre(a))
print(a[-1]-a[0])
