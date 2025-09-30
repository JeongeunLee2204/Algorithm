#20250930
#2606 바이러스
#DFS

import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
a=[[] for _ in range(n+1)]
for _ in range(m):
    s,e=map(int,input().split())
    a[s].append(e)
    a[e].append(s)

visited=[False]*(n+1)
def DFS(v):
    visited[v]=True
    for i in a[v]:
        if not visited[i]:
            DFS(i)
DFS(1)
#print(visited)
print(sum(visited)-1)