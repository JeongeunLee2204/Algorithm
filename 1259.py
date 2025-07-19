# 20250719
# 1259 팰린드롬수
# 구현
# 아이디어: 원래 수를 반전한 수rev와 원래 수 original이 같은가?
def isPal(n):
    original = n
    rev = 0

    while n>0:
        rev=rev*10+n%10
        n=n//10
    return rev==original

while True:
    n = int(input())
    if n == 0:
        break
    if isPal(n):
        print("yes")
    else:
        print("no")
