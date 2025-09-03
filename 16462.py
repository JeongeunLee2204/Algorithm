#20250709
#16462 '나교수' 교수님의 악필
#구현

import math

def numChange(a):
    for i in range(len(a)):
        if a[i]=='0' or a[i]=='6' or a[i]=='9':
            a[i]='9'
    return int(''.join(a))

n=int(input())
result=[]
for _ in range(n):
    a=list(input())
    if numChange(a)>100:
        result.append(100)
    else:
        result.append(numChange(a))

print(math.floor(sum(result) / len(result) + 0.5))
#python에서 round를 쓰면 n.5 는 n+1이 아닌 n이 되어버림
#floor(내림)을 쓰면 .5 정상적으로 처리가능
#원리: 1.5->2->(floor)->2
# 1.7->2.2->floor->2
# 1.3->1.8->floor->1