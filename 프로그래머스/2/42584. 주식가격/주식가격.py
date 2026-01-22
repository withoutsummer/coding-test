def solution(prices):
    n = len(prices)
    idx_st= [] # 아직 가격이 떨어진 적 없는 인덱스
    answer =[0]*n # j시점 가격이 처음으로 떨어지는 시점까지 걸린 시간
    
    for i,cur in enumerate(prices):
        
        # print("i:",i,"cur:",cur)
        # print("idx_st:",idx_st)
        # 가격이 떨어지는 순간 / 이전 인덱스 값 현재 값보다 클 수 있으므로 while문으로 반복
        while idx_st and prices[idx_st[-1]] > cur:
            j = idx_st.pop() # 스택 맨 위 인덱스
            # print("j:", j)
            answer[j] = i - j
            # print("idx_st:",idx_st,"answer:",answer)
        # 현재 인덱스는 떨어지지 않은 스택이므로 저장    
        idx_st.append(i)
        
    # 최종 떨어지지 않은 인덱스를 배열 길이에서 빼서 기간 계산
    while idx_st:
        j = idx_st.pop()
        answer[j] = (n-1)-j
        
    
    return answer