#20250815
#1931 회의실 배정
#그리디

import sys
input = sys.stdin.readline

n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]

def sort_key(meeting):
    start, end = meeting
    return (end, start)

a.sort(key=sort_key)

count = 0
end_time = -1

for s, e in a:
    if s >= end_time:
        count += 1
        end_time = e

print(count)
