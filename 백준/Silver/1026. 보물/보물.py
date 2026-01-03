import sys
input = sys.stdin.readline

N= int(input())
A= list(map(int,input().split()))
B= list(map(int,input().split()))
result = 0

A.sort()
B_sorted = sorted(B,reverse=True)

for i in range(N):
    result += A[i] * B_sorted[i]

print(result)