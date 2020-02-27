#the only difference b/w binary and unbound knapsack is that we can use any items any times to maximize profit
#the only difference implementation going to make is to not increase index in situation item is picked as item cna be picked any number of times give capacity doesn't breach
import math

def unbounded_knapsack(profits, weights, capacity, index):
    if capacity <= 0 or index >= len(profits):
        return 0

    profit1 = 0
    if weights[index] <= capacity:
        profit1 = profits[index] + unbounded_knapsack(profits, weights, capacity - weights[index], index)

    profit2 = unbounded_knapsack(profits, weights, capacity, index+1)

    return max(profit1, profit2)


def coin_change(denomination, total, index=0):
    if index >= len(denomination) or len(denomination) == 0:
        return 0

    if total == 0:
        return 1

    sum1 = 0
    if denomination[index] <= total:
        sum1 = coin_change(denomination, total - denomination[index], index)

    sum2 = coin_change(denomination, total, index + 1)

    return sum1 + sum2


def min_coin_change(denominations, total, index = 0):
    if index >= len(denominations):
        return math.inf
    if total == 0:
        return 0

    count1 = math.inf
    if denominations[index] <= total:
        res = min_coin_change(denominations, total-denominations[index], index)
        if res != math.inf:
            count1 = res + 1

    count2 = min_coin_change(denominations, total, index+1)
    return min(count1, count2)


