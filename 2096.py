#20251011
#2096 내려가기
#rolling dp : dp리스트 만들지 말고 변수 1개 갱신하기(메모리 절약)
#동시대입(tuple assignment) : 동시에 대입해야 6개 변수 한번에 갱신 가능(일반 대입문 사용시 앞에서 대입된 값이 잘못 누적됨)

import sys
input=sys.stdin.readline

n=int(input())
n1,n2,n3=(list(map(int,input().split())))

dp1=n1
dp2=n2
dp3=n3
mdp1=n1
mdp2=n2
mdp3=n3
for _ in range(n-1):
    n1, n2, n3 = (list(map(int, input().split())))

    dp1, dp2, dp3, mdp1, mdp2, mdp3 = (
        n1 + max(dp1, dp2),
        n2 + max(dp1, dp2, dp3),
        n3 + max(dp2, dp3),
        n1 + min(mdp1, mdp2),
        n2 + min(mdp1, mdp2, mdp3),
        n3 + min(mdp2, mdp3)
    )

maxPoint=max(dp1,dp2,dp3)
minPoint=min(mdp1,mdp2,mdp3)
print(maxPoint, minPoint)
