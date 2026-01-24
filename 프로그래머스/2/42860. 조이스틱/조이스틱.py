def solution(name):
    n = len(name)
    upDown = 0
    
    # 알파벳 계산
    for ch in name:
    # 위로 계산과 아래로 계산에서 최솟값 선택
        ch_idx = ord(ch) - ord("A");
        upDown += min(ch_idx, 26 - ch_idx)
    
    # 2) 좌/우 이동 최소값 계산
    # 기본 : 오른쪽으로 끝까지 가는 경우
    minMove = n - 1
    
    for i in range(n):
        j = i + 1
        while j<n and name[j] == "A":
            j += 1
        
        # 1. 오른쪽 i갔다 돌아오는 경로
        frontPr = 2*i +(n-j)
        # 2. 뒤쪽을 먼저 처리하고 오른쪽을 가는 경로
        backPr = i + 2*(n-j)
        
        minMove = min(minMove,frontPr,backPr)
        
    return upDown + minMove
