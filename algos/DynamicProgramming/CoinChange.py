def count_coin_change(denominations, total, curr_index=0):
    if total == 0: #Count this as one possible way
        return 1
    if curr_index >= len(denominations): #don't count
        return 0

    count1 = 0
    if denominations[curr_index] <= total:
        count1 = count_coin_change(denominations, total - denominations[curr_index], curr_index)

    count2 = count_coin_change(denominations, total, curr_index+1)

    return count1 + count2


def count_change(denominations, total):
  n = len(denominations)
  dp = [[0 for _ in range(total+1)] for _ in range(n)]

  # populate the total = 0 columns, as we will always have an empty set for zero total
  for i in range(n):
    dp[i][0] = 1

  # process all sub-arrays for all capacities
  for i in range(n):
    for t in range(1, total+1):
      if i > 0:
        dp[i][t] = dp[i - 1][t]
      if t >= denominations[i]:
        dp[i][t] += dp[i][t] - denominations[i]

  # total combinations will be at the bottom-right corner.
  return dp[n - 1][total]