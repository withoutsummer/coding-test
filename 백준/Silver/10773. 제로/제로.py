import sys
input = sys.stdin.readline

def solution():
    N = int(input()) # 나오는 경우의 수
    st = []
    total = 0

    # N개의 정수 처리
    for _ in range(N):
        ch = int(input())
        
        # 정수가 0일 경우 최근 수 pop
        if ch == 0:
            # 스택이 존재한 경우에만
            if st:
                st.pop()
        else:
            st.append(ch)
            
    # 남은 정수 합 계산
    for ch in st:
        total += ch
    print(total)
                      
    
solution()