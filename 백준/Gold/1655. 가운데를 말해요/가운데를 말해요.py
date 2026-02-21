import sys, heapq
input = sys.stdin.readline

n = int(input())
left = []   # max-heap (음수로 저장)
right = []  # min-heap

for _ in range(n):
    x = int(input())

    # 1) 크기 맞춰 삽입
    if len(left) == len(right):
        heapq.heappush(left, -x)
    else:
        heapq.heappush(right, x)

    # 2) 순서 조건 깨지면 top 교환
    if right and (-left[0] > right[0]):
        l = -heapq.heappop(left)
        r = heapq.heappop(right)
        heapq.heappush(left, -r)
        heapq.heappush(right, l)

    # 3) 중앙값 출력(짝수면 작은 쪽 = left top)
    print(-left[0])