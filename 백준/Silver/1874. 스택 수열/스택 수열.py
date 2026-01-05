import sys
input = sys.stdin.readline

N= int(input())
st= []
ops= []
next_num = 1
possible = True

for _ in range(N):
    x = int(input())
    while next_num <= x:
        st.append(next_num)
        ops.append("+")
        next_num += 1
    
    if st and st[-1] == x:
        st.pop()
        ops.append("-")
    else:
        possible = False
        break

if possible:
    print("\n".join(ops))
else:
    print("NO")