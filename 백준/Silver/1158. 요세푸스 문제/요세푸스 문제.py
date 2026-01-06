import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())
q = deque([i+1 for i in range(N)])
result = []

while q:
    for ch in range(K-1):
        q.append(q.popleft())
    
    result.append(q.popleft())

print("<"+", ".join(map(str,result))+">")