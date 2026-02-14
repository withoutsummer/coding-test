from collections import deque
import sys
input = sys.stdin.readline

def solution():
    N = int(input()) # 나오는 경우의 수
    moves = list(map(int,input().split()))
    dq = deque((i+1,moves[i]) for i in range(N))
    out = []

    while dq:
        idx,mov = dq.popleft()
        out.append(idx)

        if mov > 0:
            dq.rotate(-(mov-1))
        else:
            dq.rotate(-mov)
            
    print(*out)
          
solution()