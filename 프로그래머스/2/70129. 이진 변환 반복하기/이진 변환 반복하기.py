


def solution(s):
    answer = []
    count = 0
    zero_sum = 0
    
    while s != "1":
        zero_sum += s.count("0")
        s = s.replace("0", "")
        c = len(s)
        ex_s = ""
        
        while c != 0:
            mok, remain = divmod(c,2)
            c = mok
            ex_s += str(remain)
            
        s = ex_s[::-1]
        count +=1
    
    answer.extend([count,zero_sum])
    return answer