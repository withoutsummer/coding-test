def solution(sizes):
    max_w = 0
    max_h = 0
    
    for w,h in sizes:
        
        # 가로를 세로보다 크도록 조건문을 통해 뒤집기
        if h > w:
            h,w = w,h
            
        # 가로와 세로에서 최대값을 찾기
        max_w = max(max_w,w)
        max_h = max(max_h,h)
        
    return max_w * max_h