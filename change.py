def change(p, g):
    p *= 100
    g *= 100
    c = g - p
    coins = [1, 5, 10, 25, 50, 100]
    change_array = [0] * len(coins)
    i = len(coins) - 1
    while i >= 0 and c > 0:
        if float(coins[i]) > float(c):
            i -= 1
        else:
            change_array[i] += 1
            c -= coins[i]
    return change_array

print change(0.99, 5)