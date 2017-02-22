
def solution(A, B, C):
    mapping = {}
    aux = {}

    for i in xrange(len(A)):
        aux[i] = i
        for j in xrange(A[i], B[i] + 1):
            if j in mapping:
                mapping[j].append(i)
            else:
                mapping[j] = []
                mapping[j].append(i)

    count = 0

    for i in xrange(len(C)):
        if C[i] in mapping:
            for e in mapping[C[i]]:
                if e in aux:
                    aux.pop(e)
        count += 1
        if len(aux) == 0:
            return count

    return -1

print solution([1, 4, 5, 8], [4, 5, 9, 10], [4, 6, 7, 10, 2])






def binary_search(A, x):
    n = len(A)
    beg = 0
    end = n - 1
    result = -1
    while beg <= end:
        mid = (beg + end) / 2
        if A[mid] <= x:
            beg = mid + 1
            result = mid
        else:
            end = mid - 1
    return result
