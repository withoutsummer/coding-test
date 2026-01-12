def solution(i, j, k):
    result = 0
    for i in range(i,j+1):
        arr = list(str(i))
        
        for ch in arr:
            if str(k) == ch:
                result += 1
            
    return result