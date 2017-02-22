def solution(A):
    srtRep = ''.join(str(e) for e in A)
    print int('10011', 2)

    intValue = 9
    result = []
    while intValue != 0:
        remainder = intValue % -2
        intValue = intValue / -2
        if remainder < 0:
            remainder += 2
            intValue += 1
        result.insert(0, remainder)

    return result

print solution([])