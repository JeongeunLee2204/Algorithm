#20250831
#1874 스택 수열

import sys

input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]

stack = []
result = []
num = 1
possible = True

for target in a:
    while num <= target:
        stack.append(num)
        result.append('+')
        num += 1

    if stack and stack[-1] == target:
        stack.pop()
        result.append('-')
    else:
        possible = False
        break

if possible:
    print("\n".join(result))
else:
    print("NO")
