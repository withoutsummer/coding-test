def solution(n, lost, reserve):
    # 1) 겹치는 학생 먼저 제거
    lost_set = set(lost)
    reserve_set = set(reserve)

    common = lost_set & reserve_set
    lost_set -= common
    reserve_set -= common

    # 2) 정렬해서 그리디 안정화
    lost_list = sorted(lost_set)
    reserve_list = sorted(reserve_set)

    total = n - len(lost_list)

    # 3) 빌려주기: 왼쪽 먼저, 없으면 오른쪽
    for l in lost_list:
        if l - 1 in reserve_set:
            reserve_set.remove(l - 1)
            total += 1
        elif l + 1 in reserve_set:
            reserve_set.remove(l + 1)
            total += 1

    return total
