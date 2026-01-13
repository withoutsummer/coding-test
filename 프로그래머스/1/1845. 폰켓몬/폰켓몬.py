def solution(nums):
    num = len(nums)/2
    nums_s = set(nums)
    
    return num if len(nums_s) > num else len(nums_s)

