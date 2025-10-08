#20251008
#1418 K-세준수
import math
import sys
input=sys.stdin.readline

# def isPrime(n):
#     if n==1:
#         return False
#     for i in range(2,int(math.sqrt(n))+1):
#         if n%i==0:
#             return False
#     return True

def KSejun(n):
    temp = n
    max_prime = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        while temp % i == 0:
            max_prime = max(max_prime, i)
            temp //= i
    if temp > 1:
        max_prime = max(max_prime, temp)
    return max_prime <= k


n=int(input())
k=int(input())

count=0
for i in range(1, n+1):
    if KSejun(i):
        count += 1
print(count)