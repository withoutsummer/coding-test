def solution(s):
    answer = False
    st = []
    if s[0] == ")" or len(s) % 2 != 0:
        return False

    if s.count("(") > len(s) // 2:
        return False
    
    for ch in s:
        if ch == "(":
            st.append(ch)
        
        else:
            if not st:
                return False
            st.pop()
        
    return True