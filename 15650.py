#20250902
#15650 n과 m(2)

n,m=map(int,input().split())
a=[i for i in range(1,n+1)]

for i in range(1,n-m+2):
    for j in range(i,i+m+1):
        print(i,j)