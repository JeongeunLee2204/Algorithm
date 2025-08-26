#20250826
#1003 피보나치 함수
#dp

import sys
input=sys.stdin.readline
t=int(input())

for _ in range(t):
    n=int(input())
    one,zero=1,0
    for i in range(n):
        one, zero=zero, one+zero
    print(one,zero)
