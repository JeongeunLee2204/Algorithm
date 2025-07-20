#20250720
#11866 요세푸스 문제 0
#큐
from collections import deque

n, k = map(int, input().split())
q = deque(range(1, n + 1))
result = []

while q:
    q.rotate(-(k - 1)) #큐 회전하기
    result.append(q.popleft())

print("<" + ", ".join(map(str, result)) + ">")
