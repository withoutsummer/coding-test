from collections import deque

M,N,H = map(int,input().split())

# 3차원 리스트 구조: [높이][세로][가로]
grid = []
visited = []

for _ in range(H):
    grid_layer = [list(map(int,input().split())) for _ in range(N)]
    visited_layer = [[False]*M for _ in range(N)]
    
    grid.append(grid_layer)
    visited.append(visited_layer)
    


# 6방향: 위, 아래, 상, 하, 좌, 우
dh = [1, -1, 0, 0, 0, 0]
dn = [0, 0, -1, 1, 0, 0]
dm = [0, 0, 0, 0, -1, 1]

q = deque()
max_days = 0 

for h in range(H):
    for n in range(N):
        for m in range(M): 
            if grid[h][n][m] == 1:
                q.append((h,n,m))
                visited[h][n][m] = True

                
while q:
    curr_h, curr_n, curr_m = q.popleft()
 
    for i in range(6):
        nh, nn, nm = curr_h + dh[i], curr_n + dn[i], curr_m + dm[i]

        if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M:
            if not visited[nh][nn][nm] and grid[nh][nn][nm] == 0:
                visited[nh][nn][nm] = True
                grid[nh][nn][nm] = grid[curr_h][curr_n][curr_m] + 1
                q.append((nh, nn, nm))
                max_days = max(max_days, grid[nh][nn][nm])
                

for h in range(H):
    for n in range(N):
        for m in range(M):
            if grid[h][n][m] == 0:
                print("-1")
                exit() # 바로 프로그램 종료

# 모든 토마토가 익었다면 날짜 출력
if max_days == 0:
    # BFS 내에서 한 번도 새로운 토마토를 익히지 않았다는 뜻 (이미 다 익어있었음)
    print(0)
else:
    # 1에서 시작해서 n까지 늘어났으므로, 걸린 일수는 n - 1
    print(max_days - 1)


                   
                    
            
