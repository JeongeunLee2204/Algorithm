#20250725
#26264 빅데이터? 정보보호!
#구현
n=int(input())
s=input()
a=s.count('security') #count로 문자열 안의 (파라미터) 세기
b=s.count('bigdata')

if a>b:
    print("security!")
elif b>a:
    print("bigdata?")
else:
    print("bigdata? security!")