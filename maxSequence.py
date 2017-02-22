


def solution(A):
    A = A[1:len(A)-1]
    max_ending = 0
    max_slice = -1000000
    max_b = 0
    max_e = 0
    for i in range(len(A)):
        if max_ending + A[i] > max_ending:
            max_ending = max_ending + A[i]
            max_b = i
        if max_ending > max_slice:
            max_slice = max_ending
            max_e = i
    print max_b, max_e

    return max_slice

print solution([3, 2, 6, -1, 4, 5, -1, 2])

# def solution(A):
#     max_profit = 0
#     min_value = 200000
#     for e in A:
#         min_value = min(min_value, e)
#         max_profit = max(max_profit, e - min_value)
#     return max_profit
#
#
# print solution([23171, 21011, 21123, 21366, 21013, 21367])



# def solution(A):
#     max_ending = -1000000
#     max_slice = -1000000
#     for e in A:
#         max_ending = max(e, max_ending + e)
#         max_slice = max(max_slice, max_ending)
#     return max_slice
#
# print solution([3, 2, -6, 4, 0])



#
# def solution(A):
#     max_sum = None
#     for i in range(len(A)):
#         sum = 0
#         for j in range(i, len(A)):
#             sum += A[j]
#             if max_sum is None:
#                 max_sum = sum
#             elif sum > max_sum:
#                 max_sum = sum
#
#     return max_sum
#
#
# print solution([5, -7, 3, 5, -2, 4, -1])