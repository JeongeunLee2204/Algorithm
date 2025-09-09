#20250909
#2644 촌수계산
#dfs

import sys
input=sys.stdin.readline

n=int(input())
a,b=map(int,input().split())
m=int(input())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for _ in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

def dfs(v, num):
    if v==b:
        return num
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            res=dfs(i,num+1)
            if res!=-1:
                return res
    return -1

ans=dfs(a,0)
print(ans)
