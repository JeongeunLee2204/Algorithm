#20250718
#32209 다음 달에 봐요
#구현
n=int(input())
problem=0
for i in range(n):
    a,b=map(int,input().split())
    if a==1:
        problem+=b
    else:
        problem-=b
    if problem<0:
        print("Adios")
        exit(0)

print("See you next month")