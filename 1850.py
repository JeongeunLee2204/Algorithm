#20250730
#1850 최대공약수
#정수론-유클리드 호제법

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

a,b=map(int,input().split())
result=gcd(a,b)

#print(result)
while result>0:
    print(1,end='')
    result-=1