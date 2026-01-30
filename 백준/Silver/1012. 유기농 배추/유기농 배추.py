import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 깊이우선방식으로 배추밭을 순회하면서 1인 밭 상하좌우 재귀함수 호출
def dfs(r,c):
     # r: row (0 ~ n-1), c: col (0 ~ m-1)
    if r < 0 or r >= n or c < 0 or c >= m:
        return False
    
    if field[r][c] == 1:
        field[r][c] = 0
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)
        return True
    return False
    

case = int(input())
for _ in range(case):
    m,n,k = map(int,input().split())
    field = [[0] * m for _ in range(n)]
    
    for _ in range(k):
        x,y = map(int,input().split())
        field[y][x] = 1
    
    # 배추밭을 순회하면서 재귀호출
    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
                result += 1
    
    print(result) 