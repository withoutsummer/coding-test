import sys
input = sys.stdin.readline


def solution():
    list = input()
    st = []
    total = 0
    prech = ''
    
    for ch in list:
        if ch == '(':
            prech = ch
            st.append(ch)
            
        if ch == ')':
            if prech == '(': # 레이저 
                st.pop()
                total += len(st)
                prech = ch # 레이저 닫고 이전 문자로 저장
            elif prech == ')': # 쇠막대기 닫음
                st.pop()
                total += 1

    print(total)
    
solution()