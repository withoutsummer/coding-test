from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
# NxM 좌표를 위한 그리드
grid = [list(input().strip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

ans =[]
q = deque()

vx = [-1,1,0,0]
vy = [0,0,-1,1]

for i in range(N):
    for j in range(N):

        # 1. 현재 칸에 집이 있고(grid[i][j] == '1')
        # 2. 아직 방문하지 않았다면(visited[i][j] == False)
        if grid[i][j] == '1' and not visited[i][j]:
            q.append((i,j))
            visited[i][j] = True
            count = 1

            while q:
                curr_x, curr_y = q.popleft()

                for k in range(4):
                    nx = curr_x + vx[k]
                    ny = curr_y + vy[k]

                    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == '1':
                        q.append((nx,ny))
                        visited[nx][ny] = True
                        count += 1

            ans.append(count)

print(len(ans))
ans.sort()
print("\n".join(map(str,ans)))
                    

        