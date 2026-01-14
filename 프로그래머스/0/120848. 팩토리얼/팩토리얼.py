def solution(n):
    m = 0
    num = 1
    while num <= n:
        m += 1
        num *= m
        
    return m-1