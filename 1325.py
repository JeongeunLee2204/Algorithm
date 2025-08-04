#20250804
#1325 효율적인 해킹
#BFS, 그래프
#백준에서 python3은 시간초과, pypy3은 통과
import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
a=[[] for i in range(n+1)]
answer=[0]*(n+1)

def BFS(v):
    visited=[False]*(n+1)
    queue=deque()
    queue.append(v)
    visited[v]=True
    while queue:
        now=queue.popleft()
        for i in a[now]:
            if not visited[i]:
                visited[i]=True
                answer[i]+=1
                queue.append(i)


for i in range(m):
    s,e=map(int,input().split())
    a[s].append(e)

for i in range(1,n+1):
    BFS(i)

maxVal=max(answer)
for i in range(1,n+1):
    if maxVal==answer[i]:
        print(i,end=' ')
