#20250902
#11586 지영 공주님의 마법 거울

import sys
input = sys.stdin.readline

n = int(input())
a = [input().rstrip() for _ in range(n)]
k = int(input())

if k == 1:
    for row in a:
        print(row)
elif k == 2:
    # 좌우 반전: 각 문자열을 뒤집기
    for row in a:
        print(row[::-1])
elif k == 3:
    # 상하 반전: 행의 순서를 뒤집기
    for row in reversed(a):
        print(row)
