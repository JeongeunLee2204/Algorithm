#20250705
#1427 소트인사이드
#선택정렬
#선택정렬은 시간복잡도가 O(n^2) 이므로 코테에서는 자주 사용하지 않음

#내림차순 정렬이므로, 최댓값을 맨 앞으로 보내야 함에 주의
import sys
print=sys.stdout.write

a=list(input())

for i in range(len(a)):
    maxIndex=i
    #최댓값 찾기
    for j in range(i+1,len(a)):
        if a[j]>a[maxIndex]:
            maxIndex=j
    #swap
    tmp=a[maxIndex]
    a[maxIndex]=a[i]
    a[i]=tmp

for i in range(len(a)):
    print(a[i])