# 20250703
# 1377 버블 정렬 프로그램 1
# 문제에서 햇갈린 점: 주어진 c++ 코드에서, i<=n+1 이 아니라 i<n+1 아닌가?
# 답: i=1일때, i=n 까지는 일반적인 버블정렬이 실행됨. n번째 루프에서도 버블정렬이 일어났을 때,
# 이를 검출하기 위해 (내부 루프는 실행되지 않지만) 마지막 루프를 한번 더 돌려야함: 그러므로 i=n+1일때도 실행되어야 함.

# bool change = false;
# for (int i=1; i<=n+1; i++) {
#     change = false;
#     for (int j=1; j<=n-i; j++) {
#         if (a[j] > a[j+1]) {
#             change = true;
#             swap(a[j], a[j+1]);
#         }
#     }
#     if (change == false) {
#         cout << i << '\n';
#         break;
#     }
# }

import sys
#sys.stdin.readline() 로 하면 str로 인식하는 에러
#해결방법: 버블정렬에서 데이터의 정렬 전 index와 정렬 후 index를 비교해 왼쪽으로 (가장 많이 이동한 값) +1(무의미한 루프) 하면 문제의 답이 됨
input=sys.stdin.readline

n=int(input())
a=[]
MAX=0

for i in range(n):
    a.append((int(input()),i))

sa=sorted(a)

for i in range(n):
    if MAX<sa[i][1]-i:
        MAX=sa[i][1]-i
print(MAX+1)