import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))

freq = {}
result = []

for x in A:
    freq[x] = freq.get(x,0) +1

for x in arr:
    cnt=freq.get(x,0)
    result.append(cnt)
    
print(" ".join(map(str,result)))