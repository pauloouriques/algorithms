def solution(A):
    n = len(A)
    fib = [0] * (n + 2)
    fib[1] = 1
    max_n = 0
    for j in xrange(2, n + 2):
        fib[j] = fib[j - 1] + fib[j - 2]
        if fib[j] >= n:
            max_n = j
            break

    if fib[max_n] == len(A) + 1:
        return fib[max_n]
    max_n -= 1

    count = 0
    left = len(A)

    while max_n > 0:
        while fib[max_n] > left + 1:
            max_n -= 1
        if fib[max_n] == left + 1:
            count += 1
            break
        if A[len(A) - left + fib[max_n] - 1] == 1:
            count += 1
            left -= fib[max_n]
            while fib[max_n] < left:
                max_n += 1
        else:
            max_n -= 1

    if max_n == 0:
        return -1
    return count

print solution([0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0])
print solution([0, 0, 1, 0, 0])
print solution([])
print solution([0,0,0,0,1,0,1,0,0,0, 0])


# def solution(A, B):
#     result = [0] * len(A)
#     n = max(A)
#     fib = [0] * (n + 2)
#     fib[1] = 1
#     for j in xrange(2, n + 2):
#         fib[j] = fib[j - 1] + fib[j - 2]
#     for i in range(len(A)):
#         n = A[i] + 1
#         result[i] = int(fib[n] % (2 ** B[i]))
#     return result
#
# print solution([4, 4, 5, 5, 1], [3, 2, 4, 3, 1])


# def fibonacci(n):
#     f = ((1+math.sqrt(5))/2)**n
#     s = ((1-math.sqrt(5))/2)**n
#     return (f - s)/math.sqrt(5)
#
#
# print fibonacci(6)