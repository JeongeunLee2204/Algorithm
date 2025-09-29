# 20250929
# 14938 서강그라운드
# BFS(X) Floyd–Warshall(O)
# BFS는 간선 가중치 반영X, 다익스트라나 플로이드-워셜 써야함

# import sys
# from collections import deque
# input = sys.stdin.readline
#
# n, m, r = map(int, input().split())
# item = list(map(int, input().split()))
#
# a = [[] for _ in range(n + 1)]
# for _ in range(r):
#     s, e, l = map(int, input().split())
#     a[s].append([e, l])
#     a[e].append([s, l])
#
# print(item)
# print(a)
#
# def BFS(v, count):
#     visited = [False] * (n + 1)
#     q = deque([v])
#     visited[v] = True
#     count = 0
#
#     while q:
#         u = q.popleft()
#         count += item[u - 1]
#         for nxt, w in a[u]:
#             if not visited[nxt] and w <= m:
#                 visited[nxt] = True
#                 q.append(nxt)
#     return count
#
# result = []
# for i in range(1, n + 1):
#     result.append(BFS(i, 0))
#
# print(max(result))
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
item = list(map(int, input().split()))

a = [[] for _ in range(n + 1)]
INF = 10**9
dist = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dist[i][i] = 0

for _ in range(r):
    s, e, l = map(int, input().split())
    a[s].append([e, l])
    a[e].append([s, l])
    if l < dist[s][e]:
        dist[s][e] = l
        dist[e][s] = l

# Floyd–Warshall
for k in range(1, n + 1):
    for i in range(1, n + 1):
        if dist[i][k] == INF:
            continue
        for j in range(1, n + 1):
            nd = dist[i][k] + dist[k][j]
            if nd < dist[i][j]:
                dist[i][j] = nd

ans = 0
for i in range(1, n + 1):
    total = 0
    for j in range(1, n + 1):
        if dist[i][j] <= m:
            total += item[j - 1]
    if total > ans:
        ans = total

print(ans)
