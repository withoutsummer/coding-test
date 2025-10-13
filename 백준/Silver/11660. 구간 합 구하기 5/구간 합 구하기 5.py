import sys

input = sys.stdin.readline
# n은 리스트 크기, m은 질의 수
n, m = map(int,input().split())
A = [[0]*(n+1)]  # 원본 리스트는 한 행만 먼저 생성
D = [[0]*(n+1)for _ in range(n+1)] # n+1 x n+1 행렬의 이차원 리스트 생성

# print(f"A : {A}, D:{D}")

for i in range(n):
    # 입력 값을 숫자로 변환한 리스트로 받은 후, 인덱스 0부터 시작함을 고려해서 리스트 생성
    # ex) [0, (해당 줄의 첫 숫자), (둘째 숫자), …, (n번째 숫자)]
    A_row = [0]+[int(x) for x in input().split()]
    
    # 리스트를 더함.
    A.append(A_row)
    # print(f"A.append 결과:{A}")
    
for i in range(1, n+1):
    for j in range(1,n+1):
        D[i][j] = D[i][j-1]+D[i-1][j] - D[i-1][j-1] + A[i][j]
        

for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)