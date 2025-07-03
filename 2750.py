#20250703
#2750 수 정렬하기 1
#버블정렬
#출력 잘못함: print(arr)로 배열 출력 대신 반복문+print로 1줄씩 출력되게 해야함
n=int(input())
arr=[]

def swap(a,b):
    tmp=a
    a=b
    b=tmp
    return a,b

for i in range(n):
    arr.append(int(input()))
for i in range(n-1):
    for j in range(n-1-i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=swap(arr[j],arr[j+1])
for i in range(n):
    print(arr[i])