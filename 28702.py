#20250817
#28702 FizzBuzz
#구현

import sys
input = sys.stdin.readline

nums = [input().strip() for _ in range(3)]

for i in range(3):
    if nums[i] not in ["Fizz", "Buzz", "FizzBuzz"]:
        n = int(nums[i]) + (3 - i)  # 몇 번째 뒤에 있는 숫자인지 계산
        break

if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)
