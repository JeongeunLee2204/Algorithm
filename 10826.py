#20250928
#10826 피보나치 수 4

import sys
input=sys.stdin.readline

n=int(input())
a=[0]*10001
a[1]=1
a[2]=1
for i in range(3,10001):
    a[i]=a[i-1]+a[i-2]
print(a[n])