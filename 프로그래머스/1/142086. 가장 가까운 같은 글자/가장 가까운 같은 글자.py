def solution(s):
    arr = list(s)
    count_dict = {}
    result = []
    for idx,ch in enumerate(arr):
        if count_dict.get(ch) is None:
            count_dict[ch] = idx
            result.append(-1)
        else:
            result.append(idx - count_dict[ch])
            count_dict[ch] = idx
            
    return result