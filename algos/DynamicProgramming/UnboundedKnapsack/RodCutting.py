def rod_cutting(prices, lengths, length, index=0):
    if length == 0 or index >= len(prices):
        return 0
    profit1 = 0
    if lengths[index] <= length:
        profit1 = profit1 + rod_cutting(prices, lengths, length - lengths[index], index)

    profit2 = rod_cutting(prices, lengths, length, index+1)

    return max(profit1, profit2)