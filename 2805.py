#20251002
#2805 나무 자르기
#이진 탐색
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
a=list(map(int,input().split()))
s,e=0,max(a)
def cutTree(n,a):
    r=0
    for h in a:
        if h-n>0:
            r+=h-n
    return r
ans = 0
while s <= e:
    mid = (s + e) // 2
    cut = cutTree(mid, a)

    if cut >= m:
        ans = mid
        s = mid + 1
    else:
        e = mid - 1

print(ans)