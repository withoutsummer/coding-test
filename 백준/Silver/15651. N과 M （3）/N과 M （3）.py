import sys
input = sys.stdin.readline

def dfs():
    if len(path) == M:
        print(*path)
        return
        
    for i in range(N):
        path.append(i+1)
        dfs()
        path.pop()
    
N, M = map(int,input().split())
path = []

dfs()