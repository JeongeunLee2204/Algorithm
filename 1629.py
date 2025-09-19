#20250919
#1629 곱셈
#분할 탐색
#2^32 = 2^16 * 2^16
#2^16 = 2^8 * 2^8
#... 처럼 연산횟수 줄이기
def dac(a,b,c):
    if b==1:
        return a%c

    if b%2 == 0:
        return (dac(a,b//2,c)**2)%c
    else:
        return (dac(a,b//2,c)**2*a)%c


a,b,c = map(int,input().split())
print(dac(a,b,c))