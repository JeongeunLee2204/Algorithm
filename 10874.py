#20250731
#10874 이교수님의 시험
#구현

def answer(a):
    return ((a)%5)+1

result=[]

n=int(input())
for i in range(n):
    a=list(map(int,input().split()))

    #print(a)
    count = 0
    for j in range(10):
        #print(j, a[j], answer(j))
        if a[j]==answer(j):
            count+=1
            #print(count)
    if count==10:
        result.append(i+1)


for i in range(len(result)):
    print(result[i])