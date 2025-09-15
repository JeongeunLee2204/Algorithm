#20250915
#1149 RGB거리
#dp

import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

r = [0]*(n+1)
g = [0]*(n+1)
b = [0]*(n+1)

r[1], g[1], b[1] = a[0][0], a[0][1], a[0][2]

for i in range(2, n+1):
    r[i] = min(g[i-1], b[i-1]) + a[i-1][0]
    g[i] = min(r[i-1], b[i-1]) + a[i-1][1]
    b[i] = min(r[i-1], g[i-1]) + a[i-1][2]

print(min(r[n], g[n], b[n]))
