#20250809
#10814 나이순 정렬
#카운팅정렬
n=int(input())
a=[]
sortarr=[[] for _ in range(201)]
for i in range(n):
    a.append(input().split())
    a[i][0]=int(a[i][0])

    sortarr[a[i][0]].append(a[i][1])
#print(sortarr)

for i in range(201):
    if sortarr[i]:
        for j in range(len(sortarr[i])):
            print(i,sortarr[i][j])