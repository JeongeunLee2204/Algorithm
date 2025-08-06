#20250806
#2609 최대공약수와 최소공배수
#유클리드호제법

def eu(a,b):
    if a%b==0:
        return b
    else:
        return eu(b,a%b)

x,y=map(int,input().split())
if x>y:
    gcd=eu(x,y)
else:
    gcd = eu(y, x)
print(gcd)

print(x*y//gcd)