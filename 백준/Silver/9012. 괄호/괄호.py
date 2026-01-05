import sys
input = sys.stdin.readline

N = int(input())
result =[]

for _ in range(N):
    s = input().strip()
    st = []
    isValid = True

    for ch in s:
        if ch == "(":
            st.append(ch)
        elif ch == ")":
            if len(st) == 0:
                isValid = False
                break
            else :
                st.pop()
 
    if st:
        isValid = False
    
    result.append("YES") if isValid else result.append("NO")

print("\n".join(map(str,result)))