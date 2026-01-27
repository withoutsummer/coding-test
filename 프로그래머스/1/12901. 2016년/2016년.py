def solution(a, b):
    week = ["","SUN","MON","TUE","WED","THU","FRI","SAT"]
    last_day= [0,31,29,31,30,31,30,31,31,30,31,30,31]
    
    ex_days = 0
    for d in range(1,a):
        ex_days += last_day[d]
        
    print(ex_days)
    total_days = ex_days + b
    w = total_days % 7 
    print(w)
    
    if w + 5 > 7:
        return week[(w + 5) % 7]
    else:
        return week[w + 5]
    
    