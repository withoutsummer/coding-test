import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline

case = int(input())
result = []

for _ in range(case):
    N, M = map(int,input().split()) 
    priorities = list(map(int,input().split()))
    cnt = Counter(priorities)
    q = deque((p,i) for i,p in enumerate(priorities))
    
    totals = 0
    
    while q:
        p,i = q.popleft()
        has_higher = any(cnt[h] > 0 for h in range(p+1,10))
        
        if not has_higher:
            cnt[p] -= 1
            totals += 1
            if i == M:
                break
        else:
            q.append((p,i))
            
    result.append(totals)

print("\n".join(map(str,result)))

    
    