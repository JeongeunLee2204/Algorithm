#20250925
#1541 잃어버린 괄호


import sys
input=sys.stdin.readline

a = input().rstrip().split('-')
def termSum(s):
    b = s.split('+')
    return sum(map(int, b))

result = [termSum(a[0])]
for i in range(1, len(a)):
    result.append(termSum(a[i]))

print(result[0] - sum(result[1:]))
