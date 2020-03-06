def count_subset_sum(arr, sum, curr_index=0):
    if sum == 0:
        return 1
    if curr_index == len(arr):
        return 0
    sum1 = 0
    if arr[curr_index] <= sum:
        sum1 = count_subset_sum(arr, sum-arr[curr_index], curr_index+1)
    sum2 = count_subset_sum(arr, sum, curr_index+1)

    return sum1 + sum2


def count_subset_sum(arr, sum):
    dp = [[-1 for _ in range(sum+1)] for _ in range(len(arr))]

    for i in range(len(arr)):
        dp[i][0] = 1 #empty set will always form 0 sum

    for j in range(1, sum+1): # with number at 0 index you can build subset sum only when that number is equal to sum
        dp[0][j] = 1 if arr[0] == j else 0

    for num in range(1, len(arr)):
        for sum_till in range(1, sum+1):
            dp[num][sum_till] = dp[num-1][sum_till] #exclude the number

            if sum_till >= num[i]: # include this element and club with sum-this number
                dp[num][sum_till] += dp[num-1][sum_till-arr[i]]

    return dp[len(arr)-1][sum]

