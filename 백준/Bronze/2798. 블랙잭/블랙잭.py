import sys
input = sys.stdin.readline

def solution():
    N, M = map(int,input().split()) # 정수 개수, 딜러 숫자
    cards = list(map(int,input().split())) # 카드 N개의 숫자 리스트
    cards.sort(reverse = True) # 카드 숫자 내림 차순
    
    hap = 0
    min_num =  cards[-1]  # 리스트 최솟값 정수
    best = 0

    for i in range(N-2):
        fs_cd = cards[i]

        for j in range(i+1, N-1):
            sc_cd = cards[j]
            
            if fs_cd + sc_cd >= M:
                continue
                
            if fs_cd + sc_cd + min_num == M: # 목표 M과 동일하므로 최대합 결과 바로 출력
                print(fs_cd + sc_cd + min_num)
                return
            else:
                hap = fs_cd + sc_cd
                for k in range(j+1, N):
                    
                    th_cd = cards[k]
                    
                    if hap + th_cd == M: # 최대 목표값과 동일할 경우, 바로 출력
                        print(hap + th_cd)
                        return
                    elif hap + th_cd > M:
                        continue
                    else:
                        best = max(best, hap + th_cd)          
                
    print(best)

solution()