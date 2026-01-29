import sys
input = sys.stdin.readline

def solution(N):
    d = len(str(N))
    start = max(1,N-9*d)

    for m in range(start,N):
        s = sum(int(i) for i in str(m))
        if m + s == N: # 생성자 찾은 경우
            return m
        
    return 0 # 생성자가 없을 경우
        

N = int(input().strip())
print(solution(N))