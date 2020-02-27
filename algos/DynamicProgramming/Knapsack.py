
def knapsack(weights, profits, capacity, index):
    memo =[ -1 for x in range(len(weights)+1)]
    return binary_knapsack_with_memoization(weights, profits, capacity, index, memo)


def binary_knapsack(weights, profits, capacity, index):
    if index >= len(weights) or capacity <= 0:
        return 0

    profit_if_picked = 0
    if capacity >= weights[index]:
        profit_if_picked = profits[index] + binary_knapsack(weights, profits, capacity - weights[index], index + 1)

    profit_if_not_picked = binary_knapsack(weights, profits, capacity, index+1)

    return max(profit_if_picked, profit_if_not_picked)


def binary_knapsack_with_memoization(weights, profits, capacity, index, memo):
    if index >= len(weights) or capacity <= 0:
        return 0

    if memo[index] != -1:
        return memo[index]

    profit_if_picked = 0
    if capacity >= weights[index]:
        profit_if_picked = profits[index] + binary_knapsack(weights, profits, capacity - weights[index], index + 1)

    profit_if_not_picked = binary_knapsack(weights, profits, capacity, index+1)

    memo[index] = max(profit_if_picked, profit_if_not_picked)

    return memo[index]
