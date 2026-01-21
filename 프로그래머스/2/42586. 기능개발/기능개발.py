def solution(progresses, speeds):
    n = len(progresses)
    days =[] # 배포 가능한 요일
    
    for i,(pr,sp) in enumerate(zip(progresses,speeds)):
        if (100-pr) % sp == 0:
            days.append((100-pr)//sp)
        else:
            days.append(((100-pr)//sp)+1)
        
    result = []
    current_release_day = days[0]
    count = 1
    for v in days[1:]:
        if v <= current_release_day:
            count += 1
        else:
            result.append(count)
            current_release_day = v
            count = 1
    result.append(count)        
    return result