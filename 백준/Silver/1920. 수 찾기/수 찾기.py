import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

m= int(input())
arr = list(map(int,input().split()))
s= set(A)

for i in arr:
    if i in s:
        print(1)
    else:
        print(0)