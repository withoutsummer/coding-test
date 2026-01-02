import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
q = deque()
out = []

for _ in range(N):
    cmd = input().split()
    if cmd[0] == "push_front":
        q.appendleft(int(cmd[1]))
    elif cmd[0] == "push_back":
        q.append(int(cmd[1]))
    elif cmd[0] == "pop_front":
        out.append(str(q.popleft()) if q else "-1")
    elif cmd[0] == "pop_back":
        out.append(str(q.pop()) if q else "-1")
    elif cmd[0] == "size":
        out.append(str(len(q)))
    elif cmd[0] == "empty":
        out.append("1" if not q else "0")
    elif cmd[0] == "front":
        out.append(str(q[0]) if q else "-1")
    elif cmd[0] == "back":
        out.append(str(q[-1]) if q else "-1")

print("\n".join(out))