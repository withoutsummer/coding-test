from collections import deque
import sys
input = sys.stdin.readline

N = int(input()) # 컴퓨터 수
M = int(input()) # 컴퓨터 쌍의 수

# 무방향 인접 리스트로 구현
adj = [[] for _ in range(N+1)]
visited = [False]*(N+1)

for i in range(M):
    a, b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
    
# bfs
def bfs(start):
    q = deque([start])
    visited[start] = True
    count = 0

    while q:
        v = q.popleft()
        count += 1
    
        for nv in adj[v]:
            if not visited[nv]:
                q.append(nv)
                visited[nv] = True
    print(count-1)

bfs(1)


    
    
    
    