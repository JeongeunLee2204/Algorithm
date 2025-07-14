#20250714
#2023 신기한 소수 찾기
#DFS
import math
import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline

def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def DFS(a):
    if len(str(a))==n: #실수: len(str) 이므로 len(a) 가 아닌 len(str(a)) 로 써야함
        print(a)
    else:
        for i in range(1,10,2):
            b=10*a+i
            #DFS에서 현재 값을 기반으로 새로운 값을 만들 때: 기존 값을 덮어쓰지 않고(a=10*a+1) 새 변수에 만들어야 모든 분기를 정확히 탐색할 수 있음
            if isPrime(b):
                DFS(b)

n=int(input())

DFS(2)
DFS(3)
DFS(5)
DFS(7)