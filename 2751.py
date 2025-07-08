#20250708
#2751 수 정렬하기 2
#병합정렬

import sys
input=sys.stdin.readline
print=sys.stdout.write

def mergeSort(s,e):
    if e<s+1:
        return
    m=int(s+(e-s)/2) # (s+e)//2 와 같음, c++에서는 오버플로우 방지 위해 s + (e - s) // 2로 씀
    mergeSort(s,m)
    mergeSort(m+1,e)
    #정렬용 배열에 정렬하면서 넣기
    for i in range(s,e+1):
        tmp[i]=a[i]
    k=s
    index1=s
    index2=m+1
    while index1<=m and index2<=e:
        if tmp[index1]>tmp[index2]:
            a[k]=tmp[index2]
            k+=1
            index2+=1
        else:
            a[k]=tmp[index1]
            k+=1
            index1+=1
    #한쪽 그룹 정렬된 후 나머지 그룹 넣기
    while index1<=m:
        a[k]=tmp[index1]
        k+=1
        index1+=1
    while index2<=e:
        a[k]=tmp[index2]
        k+=1
        index2+=1

n=int(input())
a=[0]*int(n+1) #배열은 0번지부터 시작하지만 문제와 순서 맞추기 위해 1~n번지 사용
tmp=[0]*int(n+1)

for i in range(1,n+1):
    a[i]=int(input())
mergeSort(1,n)
for i in range(1,n+1):
    print(str(a[i])+'\n') #실수: \와/ 햇갈리지 말자...
