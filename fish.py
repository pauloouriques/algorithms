def solution(A, B):
    ds = 0
    us = []
    for i in range(len(A)):
        if B[i] == 1:
            us.append(A[i])
        else:
            ds += 1
            while len(us) > 0:
                fus = us.pop()
                if A[i] < fus:
                    us.append(fus)
                    ds -= 1
                    break
    return ds + len(us)

print solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0])