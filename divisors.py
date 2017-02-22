# def solution(A):
#     peaks = []
#     for i in range(2, len(A)):
#         if A[i] < A[i - 1]:
#             if A[i - 1] > A[i - 2]:
#                 peaks.append(i - 1)
#     max_count = 0
#     for i in range(len(peaks)):
#         k = len(peaks) - i
#         if len(A) % k == 0:
#             block = len(A) / k
#             count = 0
#             for j in range(k):
#                 b = block * j
#                 f = (block * (j + 1)) - 1
#                 for e in peaks:
#                     if f >= e >= b:
#                         count += 1
#                         break
#                 if count == k:
#                     return count
#             max_count = max(max_count, count)
#     return max_count
#
# print solution([1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6])
# # print solution([0, 1, 0, 0, 0])



# def solution(A):
#     peaks = []
#     for i in range(2, len(A)):
#         if A[i] < A[i - 1]:
#             if A[i - 1] > A[i - 2]:
#                 peaks.append(i - 1)
#     if len(peaks) <= 1:
#         return len(peaks)
#     max_k = 0
#     count = 1
#     for k in range(1, len(peaks)):
#         last_peak = peaks[0]
#         for e in peaks:
#             if e != last_peak:
#                 # print abs(e - last_peak), k + 1, e , last_peak
#                 if abs(e - last_peak) <= k + 1:
#                     count += 1
#                     last_peak = e
#
#         if count > k + 1:
#             count = k + 1
#         max_k = max(max_k, count)
#         count = 1
#
#     return max_k
#
# print solution([0, 0, 0, 0, 0, 1, 0, 1, 0, 1]) == 2
# print solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]) == 3


# def solution(n):
#     i = 1
#     last = 0
#     while i * i < n:
#         if n % i == 0:
#             last = i
#         i += 1
#     if i * i == n:
#         last = i
#     return 2 * (n / last + last)
#
# print solution(30)



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
print solution(5)