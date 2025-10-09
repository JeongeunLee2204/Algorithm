#20251009
#11725 트리의 부모 찾기

import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

n=int(input())
a=[[] for _ in range(n+1)]
for _ in range(n-1):
    s,e=map(int,input().split())
    a[s].append(e)
    a[e].append(s)

visited=[False]*(n+1)
parent=[1]*(n+1)
def dfs(v):
    visited[v]=True
    for nxt in a[v]:
        if not visited[nxt]:
            parent[nxt]=v
            dfs(nxt)
dfs(1)
for i in range(2,n+1):
     print(parent[i])
