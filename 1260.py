#20250716
#1260 DFS와 BFS
#DFS,BFS
from collections import deque
n,m,v=map(int,input().split())
a=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for _ in range(m):
    s,e=map(int, input().split())
    a[e].append(s)
    a[s].append(e)

for i in range(n+1):
    a[i].sort()

def DFS(v):
    print(v,end=' ')
    visited[v]=True
    for i in a[v]:
        if not visited[i]:
            DFS(i)

def BFS(v):
    queue=deque()
    queue.append(v)
    visited[v]=True
    while queue:
        now=queue.popleft()
        print(now,end=' ')
        for i in a[now]:
            if not visited[i]:
                visited[i]=True
                queue.append(i)

DFS(v)
print()
visited=[False]*(n+1)
BFS(v)