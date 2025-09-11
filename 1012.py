# 20250911
# 1012 유기농 배추
# bfs

from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    pos = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        pos[y][x] = 1

    visited = [[False] * m for _ in range(n)]

    def bfs(r, c):
        q = deque([(r, c)])
        visited[r][c] = True
        while q:
            x, y = q.popleft()
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and pos[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny))

    cnt = 0
    for i in range(n):
        for j in range(m):
            if pos[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                cnt += 1

    print(cnt)
