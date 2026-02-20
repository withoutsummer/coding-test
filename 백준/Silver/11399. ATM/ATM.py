import sys
input = sys.stdin.readline

N =  int(input())
pr_time = list(map(int,input().split()))
pr_time.sort()
min_hap = 0
cal = 0

for i in range(N):
    if i == 0:
        cal = pr_time[i]
        min_hap = cal
        continue
        
    cal += pr_time[i]
    min_hap += cal

print(min_hap)