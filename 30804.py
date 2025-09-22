#20250922
#30804 과일 탕후루
#슬라이딩 윈도우

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

cnt = {}
left = 0
ans = 0

for right in range(n):
    x = a[right]
    cnt[x] = cnt.get(x, 0) + 1

    while len(cnt) > 2:
        y = a[left]
        cnt[y] -= 1
        if cnt[y] == 0:
            del cnt[y]
        left += 1

    ans = max(ans, right - left + 1)

print(ans)
