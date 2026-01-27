def solution(A,B):
    A.sort()
    B.sort(reverse = True)
    n = len(A)
    total = 0
    
    for i in range(n):
        total += A[i]* B[i]

    return total