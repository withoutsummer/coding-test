def solution(citations):
    citations.sort()
    n = len(citations)

    max_h = 0
    for i,c in enumerate(citations):
        h = n - i
        
        if c >= h:
            if max_h < h:
                max_h = h
                
    return max_h