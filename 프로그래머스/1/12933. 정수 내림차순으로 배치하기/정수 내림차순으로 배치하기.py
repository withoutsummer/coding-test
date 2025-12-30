def solution(n):
    answer = [ch for ch in str(n)]  # ['1','1','8','3','7','2']
    # answer.sort(reverse=True)  1-1. 원본을 바로 내림차순
    # return int("".join(answer)) 1-2. 정렬된 리스트를 합치고 정수로 변환
    
    # 2. 정렬된 새 리스트를 바로 합치고 정수로 변환
    return int("".join(sorted(answer,reverse=True))) 