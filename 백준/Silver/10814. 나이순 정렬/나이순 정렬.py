import sys
input = sys.stdin.readline

N = int(input())
members = []

for i in range(N):
    age, name = input().split()
    members.append([int(age),i,name])
    
sorted_mem = sorted(members, key = lambda x:(x[0],x[1]))

for age,idx,name in sorted_mem:
    print(age,name)
    