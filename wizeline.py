def numberToName(N):
    mapping = {}
    mapping[0] = ""
    mapping[1] = "one"
    mapping[2] = "two"
    mapping[3] = "three"
    mapping[4] = "four"
    mapping[5] = "five"
    mapping[6] = "six"
    mapping[7] = "seve"
    mapping[8] = "eigth"
    mapping[9] = "nine"
    mapping[10] = "ten"
    mapping[11] = "eleven"
    mapping[12] = "twelve"
    mapping[13] = "thirteen"
    mapping[14] = "fourteen"
    mapping[15] = "fifteen"
    mapping[16] = "sixteen"
    mapping[17] = "seventeen"
    mapping[18] = "eighteen"
    mapping[19] = "nineteen"
    mapping[20] = "twenty"
    mapping[30] = "thirty"
    mapping[40] = "fourty"
    mapping[50] = "fifty"
    mapping[60] = "sixty"
    mapping[70] = "seventy"
    mapping[80] = "eighty"
    mapping[90] = "ninety"
    mapping[100] = "hundred"
    mapping[1000] = "thousand"

    factor = 1000
    count = 0
    name = ""
    space = " "
    while factor > 0:
        if N >= factor:
            aux = N / factor
            if N < 20:
                name += " and " + mapping[aux]
            else:
                if name != "" and factor == 100:
                    name += ", "
                elif name != "" and factor == 10:
                    name += " and "
                name += mapping[aux] + space + mapping[factor]
            N = N % factor
        else:
            factor = factor / 10
            if factor == 0:
                name += mapping[N]
    return name

print numberToName(9856)