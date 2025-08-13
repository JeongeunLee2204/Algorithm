#20250813
#1032 명령 프롬프트
#문자열, 구현

n=int(input())
a=input()
result=list(a)
for _ in range(n-1):
    b=input()
    for i in range(len(a)):
        if a[i]==b[i]:
            continue
        else:
            result[i]='?'
print(''.join(result))