#20250830
#20124 모르고리즘 회장님 추천 받습니다

n=int(input())
a=[]
for _ in range(n):
    a.append(input().split())
a.sort()
a.reverse()

max=0
for i in range(n):
    if int(a[i][1])>=max:
        president=a[i][0]
        max=int(a[i][1])
print(president)