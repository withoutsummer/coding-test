import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    sizeList = list(map(int,input().split()))
    T,P = map(int,input().split())

    tBundle = 0
    pBundle = 0
    pCount = 0

    # 1. 티셔츠 배열 순환
    for i in sizeList:
        if i == 0:
            continue
        elif T >=  i:
            tBundle += 1
        elif T < i:
            tBundle += i//T if i%T == 0 else (i//T)+1

    print(tBundle)
    
    # 2. 펜 개수 구하기
    pBundle = N // P
    pCount = N % P
    print(pBundle, pCount)
            
    
    
solution()