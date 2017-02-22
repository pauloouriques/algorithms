def solution(A):
    map1 = {}
    map2 = {}
    current1 = [-1] * len(A)
    current2 = [-1] * len(A)
    max1 = 0
    max2 = 0
    j = len(A) - 1
    for i in range(len(A)):

        if A[i] in map1:
            map1[A[i]] += 1
            if map1[A[i]] > map1[max1]:
                max1 = A[i]
            if map1[max1] > (i + 1)/2:
                current1[i] = A[i]
        else:
            map1[A[i]] = 1
            max1 = A[i]
            if map1[max1] > (i + 1)/2:
                current1[i] = A[i]

        if A[j] in map2:
            map2[A[j]] += 1
            if map2[A[j]] > map2[max2]:
                max2 = A[j]
            if map2[max2] > (j + 1)/2:

                current2[j] = A[j]
        else:
            map2[A[j]] = 1
            max2 = A[j]
            if map2[max2] > (j + 1)/2:
                current2[j] = A[j]
        j -= 1

    count = 0
    for i in range(len(A)):
        print current1[i], current2[i]
        if current1[i] != -1 and current2[i] != -1:
            if current1[i] == current2[i]:
                count += 1
    return count

print solution([4, 3, 4, 4, 4, 2] )
