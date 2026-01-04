import sys
import bisect

N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
findArr = list(map(int, input().split()))

result = [0] * M

for idx, val in enumerate(findArr):
    first_i = bisect.bisect_left(A, val)
    last_i = bisect.bisect_right(A, val)
    
    if first_i == last_i:
        result[idx] = 0
    else:
        result[idx] = last_i - first_i

print("\n".join(map(str,result)))