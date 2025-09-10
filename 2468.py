#20250910
#2468 안전 영역
#bfs

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

max_h = max(max(row) for row in a)

def bfs(x, y, level, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x0, y0 = q.popleft()
        for k in range(4):
            i = x0 + dx[k]
            j = y0 + dy[k]
            if 0 <= i < n and 0 <= j < n and not visited[i][j] and a[i][j] > level:
                visited[i][j] = True
                q.append((i, j))
    return 1

ans = 0
for lv in range(0, max_h + 1):
    visited = [[False]*n for _ in range(n)]
    regions = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and a[i][j] > lv:
                regions += bfs(i, j, lv, visited)
    if regions > ans:
        ans = regions

print(ans)
