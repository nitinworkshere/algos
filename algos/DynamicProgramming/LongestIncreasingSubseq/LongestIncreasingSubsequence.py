#input = {-4,10,3,7,15} output = {-4, 3, 7, 15}

def longest_increasing_sub_seq(arr, curr=0, prev=-1):

    if curr >= len(arr):
        return 0
    # we need to ignore case where arr[curr] < arr[prev] only think about either include and call prev as curr or skip and keep curr as is
    c1 = 0
    if prev == -1 or arr[curr] > arr[prev]:
        c1 = 1 + longest_increasing_sub_seq(arr, curr + 1, curr) #see we replace prev with curr

    c2 = longest_increasing_sub_seq(arr, curr + 1, prev)
    return max(c1, c2)


def longest_increasing_sub_seq_tab(arr):
    dp = [1 for _ in range(len(arr))]
    max_length = 1
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] < arr[i] and dp[i] <= dp[j]:
                dp[i] = dp[j] + 1
                max_length = max(max_length, dp[i])
    return max_length

#the only difference from above algo in this is instead of doing +1 do +value to find sum
def max_sum_increasing_seq(arr, curr=0, prev=-1, sum=0):
    if curr >= len(arr):
        return sum
    sum1 = sum
    if prev == -1 or arr[curr] > arr[prev]:
        sum1 = max_sum_increasing_seq(arr, curr + 1, curr, sum + arr[curr])
    sum2 = max_sum_increasing_seq(arr, curr+1, prev, sum)

    return max(sum1, sum2)

def max_sum_increasing_seq_tab(arr):
    dp = [0 for _ in range(len(arr))]
    max_sum = 0
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] < arr[i] and dp[i] < dp[j] + arr[i]:
                dp[i] = dp[j] + dp[i]
                max_sum = max(max_sum, dp[i])

    return max_sum

def minimum_deletion_to_make_sorted(arr):
    return len(arr) - longest_increasing_sub_seq(arr)




print(longest_increasing_sub_seq([-4,10,3,7,15]))