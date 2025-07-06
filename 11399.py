#20250706
#11399 ATM
#선택정렬
#n<=1000, 시간제한 1초이므로 O(n^2) 이하 정렬 아무거나 써도 됨

n=int(input())
a=list(map(int,input().split()))

#선택정렬-기준 index 이후의 값 중 최솟값 찾기, 최솟값이 더 작다면(바꿔야 한다면) swap(기준 index, 최솟값)
for i in range(n):
    MinIndex=i
    for j in range(i+1,n):
        if a[j]<a[MinIndex]:
            MinIndex=j

    if a[i]>a[MinIndex]:
        tmp=a[i]
        a[i]=a[MinIndex]
        a[MinIndex]=tmp

s=[0]*n
s[0] = a[0]
#합 배열 만들기
for i in range(1,n):
    s[i]=s[i-1]+a[i]
print(sum(s))


# #합 배열 만들기
# for i in range(1,n):
#     s[0] = a[0]
#     s[i]=s[i-1]+a[i]
# print(sum(s))
# 실수: 루프 안에 s[0]=a[0]이 있으면 안되는 이유: n=1인 경우 루프 실행 안되며 누적합이 0으로 고정되는 문제 발생