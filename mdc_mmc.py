def solution(A, B):
    max_a = max(A)
    max_b = max(B)
    N = max(max_a, max_b)

    factors = [0] * (N + 1)
    i = 2
    while i * i <= N:
        if factors[i] == 0:
            k = i * i
            while (k <= N):
                factors[k] = i
                k += i
        i += 1

    count = 0
    for i in range(len(A)):
        prime_factors_a = {}
        prime_factors_b = {}
        x = A[i]
        while factors[x] > 0:
            prime_factors_a[factors[x]] = factors[x]
            x /= factors[x]
        prime_factors_a[x] = x

        x = B[i]
        while factors[x] > 0:
            prime_factors_b[factors[x]] = factors[x]
            x /= factors[x]
        prime_factors_b[x] = x

        if prime_factors_a == prime_factors_b:
            count += 1
    return count

print solution([15, 10, 3], [75, 30, 5])



# def least_common_multiple(N, M):
#     return (N*M) / greatest_common_divisor(N, M)
#
#
# def greatest_common_divisor(N, M):
#     if N % M == 0:
#         return M
#     else:
#         return greatest_common_divisor(M, N % M)
#
# print greatest_common_divisor(100, 5)
#
# # print least_common_multiple(10, 4)
#
#
# def mdc(a, b):
#     if a % b == 0:
#         return b
#     else:
#         mdc(b, a % b)