#20250920
#16928 뱀과 사다리 게임

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
board = [0] * 101
move = [0] * 101

for _ in range(n):
    a, b = map(int, input().split())
    move[a] = b
for _ in range(m):
    a, b = map(int, input().split())
    move[a] = b

def bfs(v):
    q = deque()
    visited = [False] * 101
    q.append((v, 0))
    visited[v] = True

    while q:
        now, count = q.popleft()
        if now == 100:
            return count
        for i in range(1, 7):
            nxt = now + i
            if nxt > 100:
                continue
            if move[nxt] != 0:
                nxt = move[nxt]
            if not visited[nxt]:
                visited[nxt] = True
                q.append((nxt, count + 1))
    return -1

print(bfs(1))
