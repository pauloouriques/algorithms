def solution(A):
    cur = 0
    count = 0
    stack = []
    for e in A:
        if e > cur:
            count += 1
            stack.append(e)
        elif e < cur:
            flag = False
            while len(stack) > 0:
                last = stack.pop()
                if last == e:
                    flag = True
                if last < e:
                    stack.append(last)
                    break
            if not flag:
                print e
                count += 1
        cur = e
    return count

print solution([2, 5, 1, 4, 6, 7, 9, 10, 1])