from collections import deque

def solution(progresses, speeds):
    days = []
    
    for i, p in enumerate(progresses):
        remain = 100 - p
        day = (remain + speeds[i] - 1) // speeds[i]  # math.ceil 올림 나눗셈
        days.append(day)
    

    d_days = deque(days)
    result =[]

    while d_days:
        cur = d_days.popleft()
        count = 1
    
        for i in range(len(d_days)):
        
            if cur >= d_days[0]:
                count += 1
                d_days.popleft()
            else:
                break
        
        result.append(count)
    
    return result