import sys
input = sys.stdin.readline

def solution(n):
    dp = [0]*(n+1)
    dp[1] = 1
    
    if n >= 2: dp[2] = 1
        
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    print(dp[n])
    
n = int(input())   
solution(n)
    