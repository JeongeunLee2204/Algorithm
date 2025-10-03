#20251003
#2562 최댓값

import sys
input=sys.stdin.readline

maxIndex=0
maxValue=0
for i in range(9):
    a=int(input())
    if a>maxValue:
        maxValue=a
        maxIndex=i+1
print(maxValue)
print(maxIndex)

