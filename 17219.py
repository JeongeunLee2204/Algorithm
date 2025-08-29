#20250829
#17219 비밀번호 찾기

n,m=map(int,input().split())
site=dict()
for _ in range(n):
    a,b=input().split()
    site[a]=b
for _ in range(m):
    s=input()
    print(site[s])
