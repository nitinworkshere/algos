def solve_knapsack(profits, weights, capacity, index=0, profit=0):
    if capacity == 0 or index >= len(profits):
        return profit

    profit1 = 0
    if capacity >= weights[index]:
        profit1 = solve_knapsack(profits, weights, capacity - weights[index], index+1, profit + profits[index])
    profit2 = solve_knapsack(profits, weights, capacity, index+1, profit)

    return max(profit1, profit2)

def solve_knapsack_second_way(profits, weights, capacity, index=0):
    if capacity == 0 or index >= len(profits):
        return 0

    profit1 = 0
    if capacity >= weights[index]:
        profit1 = profits[index] + solve_knapsack_second_way(profits, weights, capacity - weights[index], index+1)
    profit2 = solve_knapsack_second_way(profits, weights, capacity, index+1)

    return max(profit1, profit2)

def solve_knapsack_bottom_up(profits, weights, capacity):
    dp = [[0 for _ in range(capacity+1)] for _ in range(len(profits))]

    for c in range(1, capacity+1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    for i in range(1, len(profits)):
        for j in range(1, capacity+1):
            profit1, profit2 = 0, 0
            if weights[i] <= j:
                profit1 = dp[i-1][c-weights[i]] + profits[i]
            profit2 = dp[i-1][c]
            dp[i][c] = max(profit1, profit2)
    return dp[len(profits)-1][capacity]



print(solve_knapsack_second_way([1, 6, 10, 16], [1, 2, 3, 5], 6))
print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
print(solve_knapsack_bottom_up([1, 6, 10, 16], [1, 2, 3, 5], 6))