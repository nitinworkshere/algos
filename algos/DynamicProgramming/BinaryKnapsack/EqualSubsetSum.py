#Eventually problem is to find if we can make sum//2 from array

def equal_subset_sum(arr):
    total = sum(arr)
    return equal_subset_sum_rec(arr, total/2)


def equal_subset_sum_rec(arr, sum=0, index=0):
    if sum == 0:
        return True
    if index >= len(arr):
        return False

    if arr[index] <= sum:
        if equal_subset_sum_rec(arr, sum - arr[index], index+1):
            return True

    return equal_subset_sum_rec(arr, sum, index+1)


def equal_subset_sum_bottom_up(arr):
    N = len(arr)
    total = sum(arr)//2
    dp = [[False for _ in range(total+1)] for _ in range(len(arr))]

    for i in range(N):
        dp[i][0] = True

    for i in range(N):
        for j in range(1, total+1):
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            if j >= arr[i]:
                dp[i][j] = dp[i-1][j-arr[i]]

    return dp[N-1][total]


print(equal_subset_sum([2, 3, 4, 6]))
