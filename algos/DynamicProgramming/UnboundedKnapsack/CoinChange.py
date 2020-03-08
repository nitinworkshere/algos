def coin_change(denominations, total, index=0):
    if total == 0:
        return 1

    if index >= len(denominations):
        return 0

    count1 = 0
    if denominations[index] <= total:
        count1 = coin_change(denominations, total - denominations[index], index)

    count2 = coin_change(denominations, total, index+1)
    return count1 + count2


def count_change(denominations, total):
    n = len(denominations)
    dp = [[0 for _ in range(total + 1)] for _ in range(n)]

    # populate the total = 0 columns, as we will always have an empty set for zero total
    for i in range(n):
        dp[i][0] = 1

    # process all sub-arrays for all capacities
    for i in range(n):
        for t in range(1, total + 1):
            if i > 0:
                dp[i][t] = dp[i - 1][t]
            if t >= denominations[i]:
                dp[i][t] += dp[i][t - denominations[i]]

    # total combinations will be at the bottom-right corner.
    return dp[n - 1][total]


print(coin_change([1,2,3], 5))