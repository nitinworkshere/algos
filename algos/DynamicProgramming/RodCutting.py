#this is an unbounded knapsack problem
def rod_cutting(prices, lengths, length, current_index = 0):
    if length == 0 or current_index == len(lengths):
        return 0

    profit1 = 0
    if lengths[current_index] <= length:
        profit1 = prices[current_index] + rod_cutting(prices, lengths, length-lengths[current_index], current_index) #notice no increament in length

    profit2 = rod_cutting(prices, lengths, length, current_index+1)

    return max(profit1, profit2)

