import sys
input = sys.stdin.readline

N = int(input())  # n개의 정수
s = set(map(int,input().split()))

M = int(input())  # n개의 정수
findArr = list(map(int,input().split()))
result = []

for i in findArr:
    if i in s:
        result.append(1)
    else:
        result.append(0)
        
print(" ".join(map(str,result)))
         