from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# NxM 좌표를 위한 그리드
grid = [list(input().strip()) for _ in range(N)]

# -1이면 방문하지 않은 좌표임을 의미하는 그리드
dist = [[-1] * M for _ in range(N)]
q = deque()

# 시작 좌표를 (0,0)
q.append((0, 0))

# 시작 좌표는 방문했음을 표시 및 최단 경로 횟수 누적
dist[0][0] = 0  

# 현재 좌표의 상하좌우 이동을 위한 행,열 리스트
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

while q:
    r, c = q.popleft() # 현재 좌표 (r,c)
    if (r, c) == (N-1, M-1):
        break

    # 현재 좌표 기준 상하좌우 확인
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        # 조건1. NxM 범위를 벗어난 경우 넘기기
        if not (0 <= nr < N and 0 <= nc < M):
            continue
        # 조건2. 좌표가 못 가는 칸일 경우 넘기기
        if grid[nr][nc] == '0':   
            continue
        # 조건3. 이미 방문한 칸일 경우 넘기기
        if dist[nr][nc] != -1:    
            continue

        dist[nr][nc] = dist[r][c] + 1 # 방문한 칸임을 누적
        q.append((nr, nc)) # 현재 이동된 좌표로 반영(이 좌표 기준 상하좌우 확인)

        
if dist[N-1][M-1] == -1:
    print(-1)
else:
    print(dist[N-1][M-1] + 1) # 마지막 도착 점도 누적
