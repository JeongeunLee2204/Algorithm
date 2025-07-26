#20250726
#2012 등수 매기기
#그리디
#예상 등수가 높은 학생한테 높은 등수를 줘야 불만도 적어짐

import sys
input=sys.stdin.readline

n=int(input())
a=[]
for _ in range(n):
    a.append(int(input()))
b=[i for i in range(1,n+1)]
a.sort()
#print(a,b)

sum=0
for i in range(n): #실수: 예시가 n=5여서 range(5) 로 하드코딩함
    sum+=abs(a[i]-b[i])

print(sum)