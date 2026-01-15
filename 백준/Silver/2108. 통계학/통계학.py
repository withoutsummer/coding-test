import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]

# 평균
print(round(sum(numbers) / n))

# 중앙값
numbers.sort()
print(numbers[n // 2])

# 최빈값
c = Counter(numbers)
max_freq = max(c.values())
modes = [num for num, freq in c.items() if freq == max_freq]
modes.sort()

if len(modes) > 1:
    print(modes[1])
else:
    print(modes[0])

# 범위
print(numbers[-1] - numbers[0])
