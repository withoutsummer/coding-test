import sys
input = sys.stdin.readline 

def check(mid,total,requests):
    sum = 0
    for x in requests:
        if x > mid:
            sum += mid
        else:
            sum += x
    return sum <= total

def solution():
    N = int(input())
    requests = list(map(int,input().split()))
    totals = int(input())
    result = 0

    if sum(requests) <= totals:
        print(max(requests))
        return
    
    start, end = 0, max(requests)
    while start <= end:
        mid = (end + start) // 2
        if check(mid, totals, requests):
            result = mid
            start = mid + 1
        else:
            end = mid - 1       
    print(result)

    
solution()
            