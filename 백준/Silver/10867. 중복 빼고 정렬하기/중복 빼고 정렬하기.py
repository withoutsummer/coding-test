import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
sorted_s = sorted(set(arr))

print(" ".join(map(str,sorted_s)))