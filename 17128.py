#20250829
#17218 비밀번호 만들기

a=input()
b=input()
result=[]
for i in range(len(a)):
    for j in range(i,len(b)):
        if a[i]==b[j]:
            result.append(a[i])
            break

print(result)