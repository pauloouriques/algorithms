def negabinary(value):
    result = []
    while value != 0:
        remainder = value % -2
        value = value / -2
        if remainder < 0:
            remainder += 2
            value += 1
        result.insert(0, remainder)
    print result

negabinary(20)