#20250811
#21736 헌내기는 친구가 필요해
#bfs

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
campus = []
start = None

for i in range(n):
    row = list(input().strip())
    campus.append(row)
    if 'I' in row:
        start = (i, row.index('I'))

#print(campus)

dq=deque([start])
visited=[[False]*m for _ in range (n)]
visited[start[0]][start[1]] = True
cnt = 0

while dq:
    x,y=dq.popleft()
    if campus[x][y]=='P':
        cnt+=1
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            if campus[nx][ny]!='X':
                visited[nx][ny]=True
                dq.append((nx,ny))
print(cnt if cnt>0 else 'TT')