#20250724
#1715 카드 정렬하기
#그리디

from queue import PriorityQueue
n=int(input())
pq=PriorityQueue()

for _ in range(n):
    pq.put(int(input()))

a=0
b=0
sum=0
while pq.qsize()>1:
    a=pq.get()
    b=pq.get()
    sum+=a+b
    pq.put(a+b)

print(sum)