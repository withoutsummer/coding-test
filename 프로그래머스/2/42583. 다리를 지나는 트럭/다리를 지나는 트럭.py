from collections import deque

def solution(bridge_length, weight, truck_weights):
    waiting = deque(truck_weights)           # 대기 트럭
    bridge = deque([0] * bridge_length)      # 다리 위 상태. 길이만큼 0으로 시작
    time = 0
    cur_weight = 0                           # 현재 다리 위 트럭 무게 합

    # 대기 트럭이 남아있거나. 다리 위에 트럭이 남아있으면 계속 진행
    while waiting or cur_weight > 0:
        # 1) 1초가 지나며 다리가 한 칸 전진. 맨 앞 칸이 빠져나감
        left = bridge.popleft()
        cur_weight -= left

        # 2) 새 트럭을 올릴 수 있으면 올리고. 아니면 0(빈 칸)을 올림
        if waiting and cur_weight + waiting[0] <= weight:
            t = waiting.popleft()
            bridge.append(t)
            cur_weight += t
        else:
            bridge.append(0)

        # 3) 시간 1초 증가
        time += 1

    return time
