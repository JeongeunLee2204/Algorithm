#20250820
#11383 뚊
#구현, 문자열

n, m = map(int, input().split())
a = []
b = []
Eyfa = True

def double_a(s):
    result = ''
    for char in s:
        result += char * 2
    return result

for _ in range(n):
    a.append(input())

for _ in range(n):
    b.append(input())

for i in range(n):
    if b[i] != double_a(a[i]):
        Eyfa = False
        break

if Eyfa:
    print('Eyfa')
else:
    print('Not Eyfa')