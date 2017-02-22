def solution(A):
    if len(A) <= 1:
        return [0]

    aux = [0] * ((2 * len(A)) + 1)
    aux_bigger = [0] * ((2 * len(A)) + 1)
    aux_lower = [0] * ((2 * len(A)) + 1)

    for i in range(len(A)):
        aux[A[i]] += 1


    count = 0
    for i in range((len(aux_bigger) - 2), -1, -1):
        count += aux[i + 1]
        aux_bigger[i] = count

    count = 0
    for i in range(1, len(aux_lower)):
        count += aux[i - 1]
        aux_lower[i] = aux[i] + count

    result = []
    for j in range(len(A)):
        count = 0
        i = 1
        n = A[j]
        while i * i < n:
            if n % i == 0:
                if aux[i] > 0:
                    count += aux[i]
                if aux[n / i] > 0:
                    count += aux[n / i]
            i += 1
        if i * i == n and aux[i * i] > 0:
            count += aux[i]

        print count, aux_lower[n], aux_bigger[n]
        temp = aux_lower[n] - count + aux_bigger[n]
        if temp < 0:
            temp = 0
        result.append(temp)

    return result

print solution([3, 4])
#1,2,3,3,6

#
def solution(n):
    count = 0
    i = 1
    while i * i < n:
        if n % i == 0:
            count += 2
        i += 1
    if i * i == n:
        count += 1
    return count
# print solution(6)



# def solution(N, P, Q):
#     factors = [0] * (N + 1)
#     i = 2
#     while i * i <= N:
#         if factors[i] == 0:
#             k = i * i
#             while (k <= N):
#                 factors[k] = i
#                 k += i
#         i += 1
#
#     semiPrimeAmount = [0] * (N + 1)
#     indexes = [0] * (N + 1)
#
#     for i in range(2, N + 1):
#         primeFactors = []
#         k = i
#         while (factors[k] > 0):
#             primeFactors += [factors[k]]
#             k /= factors[k]
#         primeFactors += [k]
#         indexes[i] = i
#         if len(primeFactors) == 2:
#             semiPrimeAmount[i] = 1 + semiPrimeAmount[i - 1]
#         else:
#             semiPrimeAmount[i] = semiPrimeAmount[i - 1]
#     result = []
#     for i in range(len(P)):
#         result.append(semiPrimeAmount[Q[i]] - semiPrimeAmount[P[i] - 1])
#     return result
#
# print solution(26, [1, 4, 16], [26, 10 , 20])





# def sieve(n):
#     sieve = [True] * (n + 1)
#     sieve[0] = sieve[1] = False
#     i = 2
#     while i * i <= n:
#         if sieve[i]:
#             k = i * i
#             while (k <= n):
#                 sieve[k] = False
#                 k += i
#         i += 1
#     return sieve
#
# print sieve(10)