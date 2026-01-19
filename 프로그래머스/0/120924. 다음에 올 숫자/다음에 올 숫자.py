def solution(common):
    diff = common[1] - common[0]
    if common[2] - common[1] == diff:
        # 등차
        return common[0] + (len(common))*diff
    else:
        ratio = common[1] // common[0]
        return common[0]*(ratio **(len(common)))
        