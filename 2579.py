#20250904
#2579 계단 오르기

import sys
input=sys.stdin.readline

n=int(input())
a=[]
for _ in range(n):
    a.append(int(input()))
dp=[0]*(n+1)
dp[1]=a[0]
if n>=2:
    dp[2]=a[0]+a[1]
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 2] + a[i-1], dp[i - 3] + a[i - 2] + a[i-1])

#print(a)
#print(dp)
print(dp[n])