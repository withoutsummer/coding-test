import sys
from collections import deque
input = sys.stdin.readline

def bfs(N,grid):
    visited = [[-1]* N for _ in range(N)]
    vx = [-1,1,0,0]
    vy = [0,0,-1,1]
    
    q = deque([(0,0)])
    visited[0][0] = 0
    
    while q:
        nx,ny = q.popleft()
        
        if nx == N-1 and ny == N-1:
            return visited[nx][ny]
        
        for i in range(4):
            curr_x,curr_y = nx + vx[i], ny + vy[i]
            
            if 0 <= curr_x < N and 0 <= curr_y < N and visited[curr_x][curr_y] == -1:
                if grid[curr_x][curr_y] == 1:
                    visited[curr_x][curr_y] = visited[nx][ny]
                    q.appendleft((curr_x,curr_y))
                else:
                    visited[curr_x][curr_y] = visited[nx][ny] + 1
                    q.append((curr_x,curr_y))
        
    return -1           
                    
N = int(input()) # 방의 수
grid = [list(map(int,input().strip())) for _ in range(N)]                 
print(bfs(N,grid))           
            
    
    