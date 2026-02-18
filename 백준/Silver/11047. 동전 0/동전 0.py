import sys
input = sys.stdin.readline

def solution():
    N, K = map(int,input().split())
    kinds = []
    result = 0
    
    for _ in range(N):
        kinds.append(int(input()))
        
    for kind in kinds[::-1]:
        if kind > K:
            continue
        
        result += K // kind
        K %= kind
        
        if K == 0:
            print(result)
            return
        
    print(result)
    
solution()