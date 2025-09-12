#20250912
#9465 스티커
#dp

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    top = [0] + list(map(int, input().split()))
    bot = [0] + list(map(int, input().split()))

    if n == 1:
        print(max(top[1], bot[1]))
        continue

    up = [0]*(n+1)
    dn = [0]*(n+1)

    up[1] = top[1]
    dn[1] = bot[1]
    for i in range(2, n+1):
        up[i] = max(dn[i-1], dn[i-2]) + top[i]
        dn[i] = max(up[i-1], up[i-2]) + bot[i]

    print(max(up[n], dn[n]))
