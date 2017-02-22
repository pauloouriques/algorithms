def solution(A):
    intResult = []
    for i in range(len(A)):
        intResult.append(A[i] * (-2) ** i)
    value = 0
    for i in range(len(intResult)):
        value += intResult[i]

    print value
    intValue = value * -1
    print intValue
    result = []
    while intValue != 0:
        remainder = intValue % -2
        intValue = intValue / -2
        if remainder < 0:
            remainder += 2
            intValue += 1
        result.insert(0, remainder)

    return result

print solution([1, 0, 0, 1, 1])