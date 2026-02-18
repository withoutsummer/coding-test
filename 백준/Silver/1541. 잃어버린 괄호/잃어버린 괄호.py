import sys
input = sys.stdin.readline

def solution():
    sums = []
    result = 0
    
    chunks = input().split('-')
    for chunk in chunks:
        chunk_sum = sum(int(x) for x in chunk.split('+'))
        sums.append(chunk_sum)
        
    result = sums[0]
    for i in sums[1:]:
        result -= i
        
    print(result)

    
solution()
