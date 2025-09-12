#연습장

n,m=map(int,input().split())
a=[[] for _ in range(n+1)]
visited=[False]*(n+1)
print(a)
for i in range(n):
    x,y=map(int,input().split())
    a[x].append(y)
    a[y].append(x)

def dfs(v,count):
    count+=1
    visited[v]=True
    for i in a[v]:
        if not visited[i]:
            dfs(v,count)
