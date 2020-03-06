def knapsack(profits, weights, capacity, current_index=0):
    if current_index >= len(weights) or capacity <= 0:
        return 0

    profit1 = 0
    if weights[current_index] <= capacity: #current item weight is less or equal to remaining capacity
        profit1 = profits[current_index] + knapsack(profits, weights, capacity - weights[current_index], current_index+1)

    profit2 = knapsack(profits, weights, capacity, current_index+1) #Item is skipped and not participating in this

    return max(profit1, profit2)

#make a dp of n_items*(capacity+1)
def knapsack_tab(profits, weights, capacity):
    dp = [[0 for _ in range(capacity+1)] for _ in range(len(profits))]

    #fill 0 column with 0 as with 0 capacity no element can be included
    for i in range(len(profits)):
        dp[i][0] = 0

    #if only one weight we will include only if capacity is not less than the weight
    for j in range(capacity+1):
        if weights[0] <= capacity:
            dp[0][j] = weights[0]

    for row in range(len(1, profits)):
        for col in range(1, capacity+1):
            profit1 = 0
            if weights[row] <= capacity:
                profit1 = profits[row] + dp[row-1][capacity - weights[col]]
            profit2 = dp[row-1][capacity]
            dp[row][col] = max(profit1, profit2)

    return dp[len(profits)-1][capacity]





print(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
