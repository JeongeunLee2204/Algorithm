#20250828
#11650 좌표 정렬하기

import sys
input=sys.stdin.readline

n=int(input())
pos=[]
for _ in range(n):
    x,y=map(int,input().split())
    pos.append([x,y])

pos.sort() #python은 자동으로 오름차순 sort
for i in range(n):
    print(*pos[i])
