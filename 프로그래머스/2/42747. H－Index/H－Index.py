from collections import Counter

def solution(citations):
    citations.sort()
    n = len(citations)

    ok = []
    for i,c in enumerate(citations):
        h = n - i
        
        if c >= h:
            ok.append(h)
    

    if ok:
        return ok[0]
    else:
        return 0