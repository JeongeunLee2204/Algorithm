#20250728
#1934 최소공배수
#정수론-유클리드 호제법
#최소공배수 구하기=a,b곱한 다음 최대공약수로 나누기

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    result=a*b/gcd(a,b)
    print(int(result))