import sys
input = sys.stdin.readline

def dfs(start):
    # 리스트 길이가 M일 경우 언패킹으로 결과 출력 및 종료
    if len(path) == M:
        print(*path)
        return

    for i in range(start, N+1):
        #현재 정수 리스트에 추가
        path.append(i)

        # 재귀함수호출: 중복 허용되므로 i번부터 시작
        dfs(i)

        # 복귀후, 현재 정수 리스트에서 제거
        path.pop()

N,M = map(int,input().split())
path = []

dfs(1)
        