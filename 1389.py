#20250718
#1389 케빈 베이컨의 6단계 법칙
#BFS

from collections import deque
n, m = map(int, input().split())
a = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    a[s].append(e)
    a[e].append(s)


def bfs(start):
    visited = [False] * (n + 1)
    dist = [0] * (n + 1)
    visited[start] = True
    q = deque([start])

    while q:
        now = q.popleft()
        for i in a[now]:
            if not visited[i]:
                visited[i] = True
                dist[i] = dist[now] + 1
                q.append(i)

    return sum(dist[1:])


min_sum = float('inf')
min_index = 0

for i in range(1, n + 1):
    total = bfs(i)
    if total < min_sum:
        min_sum = total
        min_index = i

print(min_index)
