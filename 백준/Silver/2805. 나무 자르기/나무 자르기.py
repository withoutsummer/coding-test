import sys
input = sys.stdin.readline

def check(mid,t,arr):
    total = 0
    for x in arr:
        if x > mid:
            total += x - mid
    return total >= t

def solution():
    N, target = map(int,input().split())
    trees = list(map(int,input().split()))
    start, end = 0, max(trees)
    result = 0
    
    while end >= start:
        mid = (start + end) // 2
        
        if check(mid, target, trees):
            result = mid
            start = mid + 1
        else:
            end = mid - 1
            
    print(result)
    
solution()