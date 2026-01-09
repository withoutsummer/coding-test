import sys
input = sys.stdin.readline

def dfs():
    if len(path) == M:
        print(*path)
        return
        
    for i in range(N):
        if used[i]:
            continue
        used[i] = True
        path.append(i+1)
        dfs()
        path.pop()
        used[i] = False
    
N, M = map(int,input().split())
used = [False] * N
path = []

dfs()