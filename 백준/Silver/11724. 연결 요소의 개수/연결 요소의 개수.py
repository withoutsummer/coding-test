import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N,M = map(int,input().split())
A = [[] for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(M):
    u,v = map(int,input().split())
    A[u].append(v)
    A[v].append(u)
    

def dfs(x: int):
    visited[x] = True
    
    for nx in A[x]:
        if not visited[nx]:
            dfs(nx)
    
count = 0

for i in range(1,N+1):
    
    if not visited[i]:
        count += 1
        dfs(i)
        
        
print(count)