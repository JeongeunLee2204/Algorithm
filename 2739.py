#20250706
#2739 구구단
#단순출력-리스트 컴프리헨션, f-string 연습

n=int(input())
a=[n*x for x in range(1,10)]
for i in range(1,10):
    print(f'{n} * {i} = {a[i-1]}') #f-string 사용
