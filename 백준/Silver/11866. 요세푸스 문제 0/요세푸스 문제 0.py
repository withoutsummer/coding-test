from collections import deque
import sys
input = sys.stdin.readline

N, K=  map(int,input().split())
q = deque()
list = []

for i in range(1,N+1):
    q.append(i)

while q:
    for _ in range(K-1):
        q.append(q.popleft())

    n = q.popleft()
    list.append(n)

print(f'<{', '.join(map(str,list))}>')
    
    


    