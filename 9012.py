#20250803
#9012 괄호
#스택

t = int(input())
for _ in range(t):
    a = list(input())
    stack = []
    is_valid = True
    for ch in a:
        if ch == '(':
            stack.append(ch)
        else:  # ch == ')'
            if stack:
                stack.pop()
            else:
                is_valid = False
                break
    if stack:
        is_valid = False
    print("YES" if is_valid else "NO")
