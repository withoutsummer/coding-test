def solution(babbling):
    pronounce = ["aya", "ye", "woo", "ma"]
    count = 0

    for ba in babbling:
        i = 0
        prev_ba =""
        ok = True
        
        while i < len(ba):
            matched = False
            
            for p in pronounce:  
                
                if ba.startswith(p,i): 
                    
                    if prev_ba == p:
                        matched = False
                        break
                
                    i += len(p)
                    prev_ba = p
                    matched = True
                    break                  
                    
            if not matched:
                ok = False
                break
                        
        if ok:
            count += 1         
                
    return count

          