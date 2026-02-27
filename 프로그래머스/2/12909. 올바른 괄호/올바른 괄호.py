
from collections import deque

def solution(s):
    q = deque()
    
    for i in s:
        if i == '(':
            q.append(i)
        else:
            if not q:
                return False
            else:
                q.popleft()
            
    if not q:
        return True
    else:
        return False

    






    

# 1. '('이 나올 경우 큐에 삽입

# 2. ')'이 나올 경우
#   2-1. 큐가 빈 경우, 바로 false 리턴 
#   2-2. 큐 존재 할 경우, popleft()
# 3. 모두 돌고 아직 큐에 값이 존재할 경우 false 리턴