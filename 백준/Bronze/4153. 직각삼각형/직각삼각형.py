import sys
input = sys.stdin.readline

def solution():
    while True:
        nums = list(map(int,input().split()))

        if nums == [0,0,0]:
            break
           
        nums.sort()
        a,b,c = nums
    
        if a**2 + b**2 == c**2:
            print('right')
        else:
            print('wrong')
    
    
solution()
