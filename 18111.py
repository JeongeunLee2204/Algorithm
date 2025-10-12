#20250904
#18111 마인크래프트
#brute force, histogram

import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

height_count = [0] * 257
for row in a:
    for h in row:
        height_count[h] += 1

min_time = float('inf')
best_height = 0

for i in range(257):  # 목표 높이
    tmp_b = b
    tmp_time = 0
    for h in range(257):
        diff = h - i
        if diff > 0:
            tmp_time += 2 * diff * height_count[h]
            tmp_b += diff * height_count[h]
        elif diff < 0:
            tmp_time += (-diff) * height_count[h]
            tmp_b -= (-diff) * height_count[h]
    if tmp_b < 0:
        continue
    if tmp_time < min_time or (tmp_time == min_time and i > best_height):
        min_time = tmp_time
        best_height = i

print(min_time, best_height)
