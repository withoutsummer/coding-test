from collections import deque

def solution(priorities, location):
    q = deque((p,i) for i,p in enumerate(priorities))
    count = 0
    
    while q:
        p,idx = q.popleft()
        
        if any(p2 > p for p2,_ in q):
            q.append((p,idx))
        else:
            count += 1
            if idx == location:
                return count