#20250814
#2467 용액
#투포인터

import sys
import math
input=sys.stdin.readline

n=int(input())
a=list(map(int,(input().split())))
i=0
j=n-1
min=math.inf
mini,minj=0,0
while i<j:
    #print(i,j)
    yong=a[i]+a[j]
    #print(yong)
    if abs(yong)<min: #실수: yong이 아닌 yong의 절댓값이 최소인 경우 찾아야
        min=abs(yong)
        mini=i
        minj=j
    if yong>=0: #실수: yong>0 이면 yong==0인 경우 무한루프 발생
        j-=1
    if yong<0:
        i+=1
print(a[mini],a[minj])