def solution(k, score):
    answer = []
    arr = []
    day = 1
    
    for i in score:
        if day <= k:
            arr.append(i)
            answer.append(min(arr))
            day += 1
        else:
            arr.append(i)
            arr.sort(reverse = True)
            arr.pop()
            answer.append(arr[-1])
            day += 1
            
    return answer
            