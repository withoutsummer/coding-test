def solution(arr):
    answer = []
    ex = -1
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i,n in enumerate(arr):
        if i != 0:
            ex = arr[i-1]
        
        if ex != n:
            answer.append(n)
            
        
    return answer