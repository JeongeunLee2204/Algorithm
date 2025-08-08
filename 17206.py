#20250808
#17206 준석이의 수학 숙제
#구현
# 실수: 문장대로 구현하면 시간복잡도 n^2: 시간초과
#메모이제이션 필요
import sys
input=sys.stdin.readline

'''def func(n):
    sum=0
    for i in range(1,n+1):
        if i%3==0 or i%7==0:
            sum+=i
    return sum
'''

num=[0]*80001
sum=0

t=int(input())
a=list(map(int,input().split()))

for i in range(80001):
    if i % 3 == 0 or i % 7 == 0:
        sum+=i
    num[i]=sum

for j in a:
    print(num[j])