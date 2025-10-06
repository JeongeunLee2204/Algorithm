#20251006
#1181 단어 정렬

n=int(input())
a=list(set(input().strip() for _ in range(n))) #중복 제거 위해 set에 입력 후 list로 변환(set은 sort() 없음)

a.sort(key=lambda x: (len(x), x)) #람다 함수: 리스트의 각 원소 x를 받아서 len(x) 값을 반환. 즉, 길이를 기준으로 정렬.
print("\n".join(a))
