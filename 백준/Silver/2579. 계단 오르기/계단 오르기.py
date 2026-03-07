import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    sc = [0]* 301
    dp = [0]* 301
    
    for i in range(n):
        sc[i] = int(input())

    dp[0] = sc[0]
    dp[1] = dp[0] + sc[1]
    dp[2] = max(dp[0] + sc[2], sc[1] + sc[2])
    
    for i in range(3,n):
        dp[i] = max(dp[i-2]+sc[i], dp[i-3]+sc[i-1]+sc[i])
    
    print(dp[n-1])

solve()