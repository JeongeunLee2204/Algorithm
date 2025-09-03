#20250730
#16673 고려대학교에는 공식 와인이 있다
#구현
def wine(c,k,p):
    return k*c+p*c*c
c,k,p=map(int,input().split())
sum=0
for i in range(1,c+1):
    sum+=wine(i,k,p)
print(sum)