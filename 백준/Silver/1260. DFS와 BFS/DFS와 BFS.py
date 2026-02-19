import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N,M,V = map(int,input().split())
adj = [[] for _ in range(N+1)] # 1부터 N까지만 사용

for _ in range(M):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
    
for i in range(1,N+1):
    adj[i].sort()
    

# dfs
dfs_visited = [False]*(N+1)
dfs_order = []

def dfs(v):
    dfs_visited[v] = True
    dfs_order.append(v)
    
    for nv in adj[v]:
        if not dfs_visited[nv]:
            dfs(nv)

dfs(V)
print(*dfs_order)


# bfs
def bfs(v):
    bfs_visited = [False]*(N+1)
    bfs_order = []
    
    q = deque([v])
    bfs_visited[v] = True
    
    while q:
        v = q.popleft()
        bfs_order.append(v)
            
        for nv in adj[v]:
            if not bfs_visited[nv]:
                bfs_visited[nv] = True
                q.append(nv)
    
    print(*bfs_order)
       
bfs(V)
        
    
    

    
    

