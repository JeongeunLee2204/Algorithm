#20250715
#13023 ABCDE
#DFS
import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline

n,m=map(int,input().split())
a=[[]for _ in range(n+1)]
visited=[False]*(n+1) #방문 리스트
arrive=False

def DFS(now, depth):
    global arrive
    if depth==5: #깊이가 5면 친구관계 있으므로 arrive 를 True로 바꿈
        arrive=True
        return
    visited[now]=True
    for i in a[now]:
        if not visited[i]:
            DFS(i,depth+1) #방문 안한 노드 다시 dfs로 방문, 깊이+1
    visited[now]=False

for _ in range(m): #친구관계 입력
    s,e=map(int,input().split())
    a[s].append(e)
    a[e].append(s)

for i in range(n): #0번부터 친구관계 탐색
    DFS(i,1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)