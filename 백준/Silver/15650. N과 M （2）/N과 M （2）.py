import sys
input = sys.stdin.readline

def dfs(start):
    if len(path) == M:
        print(*path)
        return
    
    for i in range(start, N+1):
        # 리스트에 현재 정수 추가
        path.append(i)
        
        # 오름차순이므로, 현재 정수보다 +1 더한 정수를 시작으로 재귀함수 호출
        dfs(i+1)
        
        # 종료 후, 현재 정수 제거
        path.pop()
        
N, M = map(int,input().split())
path = []

dfs(1)