def solution(n):
    # 7조각 나눈 몫과 나머지가 있을 경우 +1  
    return n // 7 if not n % 7 else (n // 7) + 1