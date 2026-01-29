import sys
input = sys.stdin.readline

def solution(N):
    layer = 1
    last = 1
    while N > last:
        last += 6 * layer
        layer += 1
    
    return layer

N = int(input().strip())
print(solution(N))
    