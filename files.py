def solution(S):
    stack = []
    map = {'{':'}', '[':']', '(':')'}
    for s in S:
        if len(stack) == 0:
            if s in map.values():
                return 0
            stack.append(s)
        else:
            last = stack.pop()
            if s == map[last]:
                pass
            else:
                if s in map.values():
                    return 0
                else:
                    stack.append(last)
                    stack.append(s)

    if len(stack) == 0:
        return 1
    return 0

print solution('()()')
