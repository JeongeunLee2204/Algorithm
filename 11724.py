#20250713
#11724 연결 요소의 개수
#DFS-무방향 그래프에서 연결 요소의 개수 구하기
import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline

n,m=map(int,input().split())
a=[[]for _ in range(n+1)]
visited=[False]*(n+1)

def DFS(v):
    visited[v]=True
    for i in a[v]: #현재 노드에서 방문하지 않은 노드: 방문하기
        if not visited[i]:
            DFS(i)
for _ in range(m): #n번 노드가 연결된 노드를 리스트로 저장
    s,e=map(int,input().split())
    a[s].append(e)
    a[e].append(s)

count=0
for i in range(1,n+1):
    if not visited[i]: #방문하지 않은 노드에서 DFS새로 시작할 때마다 count+1(새로운 연결 집합)
        count+=1
        DFS(i)
print(count)