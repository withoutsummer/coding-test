def solution(arr):
    st = []
    
    for i,cur in enumerate(arr):
        # print(f"i:{i}, cur:{cur}일 때")
        
        # print(f"st: {st}")
        if not st or cur != st[-1]:
            # print(f"st에 {cur} 추가")
            st.append(cur)
            
    # print("st:",st)
    return st