#20250809
#1697 숨바꼭질
#BFS

import sys
from collections import deque

def BFS(v):
    q=deque([v])
    while q:
        v=q.popleft()
        if v==k:
            return a[v]
        for next_v in (v-1,v+1,2*v):
            if 0<=next_v<MAX and not a[next_v]:
                a[next_v]=a[v]+1
                q.append(next_v)
MAX=100001
n,k=map(int,input().split())
a=[0]*MAX
print(BFS(n))