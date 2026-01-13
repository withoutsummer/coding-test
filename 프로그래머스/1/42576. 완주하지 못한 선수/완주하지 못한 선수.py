def solution(participant, completion):
    d = {}
    
    for i in participant:
        d[i] = d.get(i, 0) + 1
        
    for i in completion:
        if i in d:
            d[i] = d.get(i, 0) - 1
            
    for k,v in d.items():
        if v != 0:
            return k
    