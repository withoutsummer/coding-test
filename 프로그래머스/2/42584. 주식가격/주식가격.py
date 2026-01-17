from collections import deque

def solution(prices):
    time_arr= []
    q_prices = deque(prices)
    
    for _ in range(len(q_prices)):
        cur = q_prices.popleft()
        count = 0
        
        for i in q_prices:
            if cur <= i:
                count += 1
            else: #현재 가격보다 클 경우, 카운트 하고 종료
                count += 1
                break
        
        time_arr.append(count)
    
    return time_arr