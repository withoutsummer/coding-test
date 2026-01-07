import sys
from collections import deque
input = sys.stdin.readline

case = int(input())
result = []

for _ in range(case):
    p = list(input().strip())
    n = int(input())
    
    arr_str = input().strip()      
    content = arr_str[1:-1] # 대괄호 삭제
    q = deque() if content == "" else deque(map(int, content.split(",")))

    isError = False
    rev = False
    
    for i in p:
        if i == "R":
            rev = not rev
        elif i == "D":
            if not q:
                isError = True
                break
            else:
                q.popleft() if not rev else q.pop()
    
    if isError:
        result.append("error")
    else:
        seq = q if not rev else reversed(q)
        result.append("[" + ",".join(map(str, seq)) + "]")
    
print("\n".join(map(str,result)))
            
    
    
    
    
