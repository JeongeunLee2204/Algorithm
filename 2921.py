#20250721
#2921 도미노
#구현

n=int(input())
total=0
for i in range(n+1):
    for j in range(i,n+1):
       total=total+(i+j)

print(total)