from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
q = deque()
MAX = 100000
dist = [-1] * (MAX + 1)   # 0~100000

q.append(N)
dist[N] = 0

while q:
    x = q.popleft()
    
    if x == K:
        print(dist[x])
        break
        
    nxts = [x-1,x+1,x*2]

    for nx in nxts:
        if ( 0 <= nx <= MAX) and dist[nx] == -1:
            if nx == x*2: # 가중치가 0이므로 앞에 추가
                dist[nx] = dist[x]
                q.appendleft(nx)
            else: # 나머지는 모두 가중치가 1이므로 뒤에 추가
                dist[nx] = dist[x] + 1
                q.append(nx)
                
            