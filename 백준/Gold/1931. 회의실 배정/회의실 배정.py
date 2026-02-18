import sys
input = sys.stdin.readline

def solution():
    N = int(input())  # 회의의 수
    meetings =[tuple(map(int, input().split())) for _ in range(N)]
    meetings.sort(key = lambda x:(x[1],x[0])) # 종료 시간 기준 오름 차순, 종료 시간 동일할 경우 시작 시간 기준 오름 차순 정렬
    
    pr_lt = -1 # 직전 회의 종료 시간
    count = 0 # 최대 회의 개수 

    for st, lt in meetings: 
        if pr_lt <= st:
            count += 1
            pr_lt = lt
            
    print(count)

solution()