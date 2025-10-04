#20251005
#2231 분해합
#brute force

import sys
input=sys.stdin.readline

n=int(input())
for i in range(1,n+1):
    a=list(map(int,str(i)))
    result=sum(a)
    #print(a,result)
    if result+i==n:
        print(i)
        break
    if i==n:
        print(0)