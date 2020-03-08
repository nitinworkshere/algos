from math import inf

def min_coin_change(denominations, total, index=0):
    if index >= len(denominations):
        return inf
    if total == 0:
        return 0

    count1 = inf
    if denominations[index] <= total:
        local_count = min_coin_change(denominations, total - denominations[index], index)
        if local_count != inf:
            count1 = local_count + 1

    count2 = min_coin_change(denominations, total, index+1)
    return min(count1, count2)


def min_coin_change(denominations, total):
    n = len(denominations)
    dp = [[inf for _ in range(total+1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = 0

    for i in range(n):
        for t in range(1, total + 1):
            if i > 0:
                dp[i][t] = dp[i - 1][t]  # exclude the coin
            if t >= denominations[i]:
                if dp[i][t - denominations[i]] != inf:
                    # include the coin
                    dp[i][t] = min(dp[i][t], dp[i][t - denominations[i]] + 1)

    return -1 if dp[n - 1][total] == inf else dp[n - 1][total]
