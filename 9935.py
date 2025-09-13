#20250913
#9935 문자열 폭발
#스택

import sys
input=sys.stdin.readline

a=input().rstrip()
s=list(input().rstrip())
l=len(s)

stack=[]
for i in a:
    stack.append(i)
    if stack[len(stack)-l:len(stack)]==s:
        for _ in range(l):
            stack.pop()
    #print(stack)
if stack:
    print(*stack, sep='')
else:
    print("FRULA")


