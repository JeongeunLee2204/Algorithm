#20250722
#1920 수 찾기
#이진탐색
n=int(input())
a=list(map(int,input().split()))
a.sort()
m=int(input())
b=list(map(int,input().split()))

for i in range(m):
    find=False
    target=b[i]

    start=0
    end=n-1
    while start<=end:
        midi=int((start+end)/2) #mid index
        midv=a[midi] #mid value
        if midv>target: #중앙값이 타겟보다 큼:왼쪽 절반 탐색
            end=midi-1
        elif midv==target: #타겟 발견
            find=True
            break
        else: #중앙값이 타겟보다 작음:오른쪽 절반 탐색
            start=midi+1
    if find:
        print(1)
    else:
        print(0)