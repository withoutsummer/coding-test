import sys
input= sys.stdin.readline

def dfs(start,path):
    
    if len(path) + (k - start) < 6:
        return

    if len(path) == 6:
        print(*path)
        return
    
    for i in range(start,k):
    
        path.append(nums[i])
        dfs(i+1,path)
        path.pop()       

while True:
    k, *nums = map(int, input().split())
    if k == 0:
        break
    
    dfs(0,[])
    print()
        
        
    
    
    
