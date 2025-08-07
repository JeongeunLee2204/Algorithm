#20250807
#31408 당직 근무표
#구현

import sys
import math
input=sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))
num=[0]*(100000+1) #병사 번호 수는 n보다 커질 수 있음-indexError발생 주의
for i in range(len(a)):
    num[a[i]]+=1
#print(num)
limit=math.ceil(n/2)
#print(limit)
if max(num)>limit:
    print('NO')
else:
    print('YES')