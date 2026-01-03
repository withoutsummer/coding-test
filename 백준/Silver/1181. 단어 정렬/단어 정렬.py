import sys
input = sys.stdin.readline

N = int(input())
s = set(input().strip() for _ in range(N))

s_sorted = sorted(s, key= lambda w:(len(w),w))

print("\n".join(s_sorted))