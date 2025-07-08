#20250707
#11004 k번째 수
#퀵정렬(퀵정렬은 pivot 선택 따라 최악 시간복잡도가 n^2이므로 병합정렬이 더 안정적, 공부를 위해 퀵정렬로 진행)

#데이터 입력받기
import sys
input=sys.stdin.readline
n,k=map(int,input().split())
a=list(map(int,input().split()))

#swap
def swap(i,j):
    global a
    tmp=a[i]
    a[i]=a[j]
    a[j]=tmp

#pviot=k이면 종료
#pivot != k 면 피벗 기준 왼쪽, 오른쪽 퀵정렬
def quickSort(s,e,k):
    global a
    if s<e:
        pivot=partition(s,e)
        if pivot==k:
            return
        elif k<pivot:
            quickSort(s,pivot-1,k)
        else:
            quickSort(pivot+1,e,k)

#피벗 구하기 함수
#데이터가 2개면 바로 정렬(swap)
#아니면 중앙값을 시작 위치와 swap 하고 pivot을 시작 위치 값(=중앙값)으로 지정
#피벗보다 큰 수가 나올 때까지 i 증가, 피벗보다 작은 수가 나올 때까지 j 감소

def partition(s,e):
    global a
    if s+1==e:
        if a[s]>a[e]:
            swap(s,e)
        return e
    m=(s+e)//2
    swap(s,m)
    pivot=a[s]
    i=s+1
    j=e

    while i<=j:
        while pivot<a[j] and j>0:
            j=j-1
        while pivot>a[i] and i<len(a)-1:
            i=i+1
        if i<=j:
            swap(i,j)
            i=i+1
            j=j-1
    a[s]=a[j]
    a[j]=pivot
    return j

#퀵정렬 실행
quickSort(0,n-1,k-1)
print(a[k-1])