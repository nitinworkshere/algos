def solve_knapsack(profits, weights, capacity=0, index=0):
    if capacity == 0 or index >= len(profits):
        return 0

    profit1 = 0
    if weights[index] <= capacity:
        profit1 = profits[index] + solve_knapsack(profits, weights, capacity - weights[index], index)

    profit2 = solve_knapsack(profits, weights, capacity, index+1)
    return max(profit1, profit2)


def solve_knapsack_bottom_up(profits, weights, capacity):

    n = len(profits)

    dp = [[0 for _ in range(capacity+1)] for _ in range(n)]

    for i in range(n):
        for j in range(1, capacity+1):
            profit1, profit2 = 0, 0
            if weights[i] <= j:
                profit1 = profits[i] + dp[i][j-weights[i]]
            if i > 0:
                profit2 = dp[i - 1][j]

            dp[i][j] = max(profit1, profit2)

    return dp[n-1][capacity]





print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 8))
print(solve_knapsack_bottom_up([15, 50, 60, 90], [1, 3, 4, 5], 8))