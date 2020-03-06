def unbounded_knapsack(profits, weights, capacity, index):
    if index >= len(profits) or capacity == 0:
        return 0
    profit1 = 0
    if weights[index] <= capacity:
        profit1 = profit1[index] + unbounded_knapsack(profits, weights, capacity-weights[index], index) #Notice we didn't increase the index instead

    profit2 = unbounded_knapsack(profits, weights, capacity, index+1)

    return max(profit1, profit2)


def unbounded_knapsack(profits, weights, capacity, index):
    n = len(profits)
    dp = [[-1 for _ in range(capacity+1)] for _ in range(len(profits))]

    for i in range(n):
        dp[i][0] = 0


    for i in range(1, n):
        for j in range(capacity+1):
            profit1, profit2 = 0, 0
            if weights[i] <= j:
                profit1 = profits[i] + dp[i][j-weights[i]] #notice we are looking in same line as item can be repeated
            profit2 = dp[i-1][j]
            dp[i][j] = max(profit1, profit2)

        return dp[n-1][capacity]
