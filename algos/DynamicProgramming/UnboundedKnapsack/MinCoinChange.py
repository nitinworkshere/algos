from math import inf
#this is an unbounded knapsack problem with a trick that we want to count all attempt done as Infinity
def min_coin_change(denominations, total, curr_index):
    if total == 0:
        return 0
    if curr_index >= len(denominations):
        return inf
    count1 = inf
    if denominations[curr_index] <= total:
        result = min_coin_change(denominations, total - denominations[curr_index], curr_index)
        if result != inf:
            count1 = result+count1
    count2 = min_coin_change(denominations, total, curr_index+1)
    return count1+count2
