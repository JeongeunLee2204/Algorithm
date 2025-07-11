#20250711
#2675 문자열 반복
#문자열

n=int(input())
for _ in range(n):
    r,s=input().split()
    r=int(r)
    result=''
    for i in range(len(s)):
       for j in range(r):
           #result.join(s[i]) 안됨: '구분자'.join(리스트) 로 사용해야함
           #join은 원본 문자열 수정하지 않고 새 문자열 반환
           result+=s[i] #문자열 직접 붙이기 위해 + 사용 / +는 문자열 많을때 느림
    print(result)