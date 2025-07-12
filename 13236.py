#20250712
#13236 Collatz Conjecture
#구현

n=int(input())
a=[n]
while 1:
    if n==1:
        break
    elif n%2==0:
        n=n//2
        a.append(n)
    else:
        n=n*3+1
        a.append(n)

print(*a) #배열 출력 시 * 붙이면 대괄호, 쉼표 없이 값만 출력됨