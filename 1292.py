#20250827
#1292 쉽게 푸는 문제
#구간합

a,b=map(int,input().split())
arr=[0]
for i in range(1,b+1):
    for j in range(i):
        arr.append(i)
sum=[arr[0]]
#print(arr)

for i in range(1, b+1):
    sum.append(sum[i-1]+arr[i])
#print(sum, sum[b], sum[a])
print(sum[b]-sum[a-1])