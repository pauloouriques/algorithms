def question(array):
    overflow = sum_array(len(array) - 1, array)
    count = 0
    while count != len(array) and overflow != 0:
        overflow = sum_array(len(array) - 1, array)

def sum_array(position, array):
    if array[position] == 9:
        array[position] = 0
        return 1
    else:
        array[position] += 1
    return 0