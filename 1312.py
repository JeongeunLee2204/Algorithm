#20250921
#소수

import sys
input = sys.stdin.readline

a,b,n = map(int, input().split())

r=a%b
for _ in range(n):
    r*=10
    d=r//b
    r%=b

print(d)
