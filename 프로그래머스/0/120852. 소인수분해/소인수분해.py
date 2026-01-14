def solution(n):
    answer = []
    finished = False
    
    # 짝수 일 경우
    if n % 2 == 0:
        answer.append(2)
        
        while n % 2 == 0:
            n = n // 2

    
    # 홀수 일경우
    p = 3
    while p*p <= n:
        if n % p == 0:
            answer.append(p)
            while n % p == 0:
                n = n // p
                
        p += 2
        
    if n > 1:
        answer.append(n)
    
    # 중복 정수 값 제거 후 리스트로 출력
    return sorted(set(answer))
    