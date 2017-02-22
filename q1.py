def solution(S):
    l = [0] * len(S)
    r = [0] * len(S)

    j = len(S) - 1
    for i in range(len(S)):
        if i == 0:
            if S[i] == "(":
                l[i] = 1
        else:
            if S[i] == "(":
                l[i] = l[i - 1] + 1
            else:
                l[i] = l[i - 1]

        if j == len(S) - 1:
            if S[j] == ")":
                r[j] = 1
        else:
            if S[j] == ")":
                r[j] = r[j + 1] + 1
            else:
                r[j] = r[j + 1]

        j -= 1
    print l
    print
    print r

    for i in range(len(S) - 1):
        if l[i] == r[i + 1]:
            return i + 1
    return 0

print solution("))))))))))))))))))))))))))(")