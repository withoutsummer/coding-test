import sys
input = sys.stdin.readline

N= int(input())
count = [0]*10001

for i in range(N):
    count[int(input())] += 1
    
    
write = sys.stdout.write
CHUNK = 1000 # 1000으로 쪼개서 출력
    
for i in range(1,10001):
    c = count[i]
    if c:
        line = f"{i}\n"
        while c > 0:
            k = CHUNK if c > CHUNK else c
            write(line*k)
            c -= k
