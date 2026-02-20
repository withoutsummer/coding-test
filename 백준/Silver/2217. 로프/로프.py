import sys
input = sys.stdin.readline

N = int(input())
rf = []
for _ in range(N):
    rf.append(int(input()))

rf.sort()
max_w = rf[0] * N

for i in range(1,N):
    max_w = max(max_w, rf[i]*(N-i))
    
print(max_w)