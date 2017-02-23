def dominoes():
    file = open("file", "r")
    result = []
    for line in file:
        line = line.strip()
        a = line.split(",")
        result.append(verify_chain(a))
    return result

def verify_chain(chain):
    max_count = 1
    count = 1
    for i in xrange(len(chain) - 1):
        if chain[i][2] == chain[i + 1][0]:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 1
    return max_count

print dominoes()