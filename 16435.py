#20250924
#16435 스네이크버드
#그리디

import sys
input=sys.stdin.readline

n,l=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
for i in a:
    if i<=l:
        l+=1
print(l)