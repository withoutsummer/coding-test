def solution(sizes):
    # 가로를 최대, 세로를 최솟값으로 정렬 수 가로, 세로 결정
    max_width, max_height = 0,0
    # print(max_width,max_height)
    
    for w,h in sizes:
        # print(w, h)
        
        if h > w :
            w, h = h,w
        
        if max_width < w:
            max_width = w
        
        if max_height < h:
            max_height = h
    
    return max_width * max_height