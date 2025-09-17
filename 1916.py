#20250917
#1916 최소비용 구하기
#다익스트라

import sys,math
input=sys.stdin.readline

n=int(input())
m=int(input())

graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
cost=[math.inf]*(n+1)

for _ in range(m):
    u,v,w=map(int,input().split())
    graph[u].append((v,w))

a,b=map(int,input().split())

def minNode():
    min=math.inf
    index=0
    for i in range(1,n+1):
        if cost[i]<min and not visited[i]:
            min=cost[i]
            index=i
    return index

def dijkstra(start):
    cost[start] = 0
    for _ in range(n):
        now = minNode()
        if now == 0 or cost[now] == math.inf:
            break
        visited[now] = True
        for v, w in graph[now]:
            if not visited[v] and cost[now] + w < cost[v]:
                cost[v] = cost[now] + w

dijkstra(a)
#print(cost)
print(cost[b])