from collections import deque
import sys
input = sys.stdin.readline

n,w,L = map(int,input().split())
trucks = deque(map(int,input().split()))

bridge = deque([0]*w)
time = 0
cur_weight = 0

while bridge:
    time += 1
    
    exit_tr = bridge.popleft()
    cur_weight -= exit_tr
    
    if trucks:
        if cur_weight + trucks[0] <= L:
            new_tr = trucks.popleft()
            cur_weight += new_tr
            bridge.append(new_tr)
        else:
            bridge.append(0)

print(time)
            
    