def subset_sum(arr, sum):
    if len(arr) == 0: # reached end but not found sum
        return False
    if sum == 0:
        return True
    return subset_sum(arr[1:], sum - arr[0]) or subset_sum(arr[1:], sum)


def subset_sum_tab(arr, sum):
    dp = [[False for _ in sum+1] for _ in range(arr)]

    for i in range(len(arr)):
        dp[i][0] = True

    for j in range(1, sum+1):
        dp[0][j] = True if arr[j] == sum else False

    for row in range(len(arr)):
        for col in range(1, sum+1):
            if dp[row-1][col]: #if sum could be acheived using previous element
                dp[row][col] = dp[row-1][col]
            elif sum[col] >= arr[row]:
                dp[row][col] = dp[row-1][col-arr[row]]

    return dp[len(arr)-1][sum+1]






print(subset_sum([1, 2, 7, 1, 5], 12))