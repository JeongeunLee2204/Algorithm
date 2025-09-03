#20250727
#33046 Alea lacta Est
#구현
import sys
input=sys.stdin.readline

A, B = map(int, input().split())
C, D = map(int, input().split())

players = [1, 2, 3, 4]

first_sum = A + B
gadong_index = (0 + (first_sum - 1)) % 4
gadong = players[gadong_index]

second_sum = C + D
jindong_index = (gadong_index + (second_sum - 1)) % 4
jindong = players[jindong_index]

print(jindong)
