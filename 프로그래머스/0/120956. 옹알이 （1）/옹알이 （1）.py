def solution(babbling):
    count = 0
    pronounce_list = ["aya", "ye", "woo", "ma"]
    
    for ba in babbling:
        i = 0
        ok = True
        
        while i < len(ba):
            matched = False
            for p in pronounce_list:
                if ba.startswith(p,i):
                    i += len(p)
                    matched = True
                    break
            
            if not matched:
                ok = False
                break
        
        if ok:
            count += 1
        
    return count
    

