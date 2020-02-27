def find_equal_subset_sum(arr):
    s = sum(arr)
    if s%2 != 0:
        return False
    return find_equal_subset_sum_recursive(arr, s/2, 0)

def find_equal_subset_sum_recursive(arr, sum, index):
    if sum == 0 or index >= len(arr):
        return False

    if arr[index] <= sum:
        if find_equal_subset_sum_recursive(arr, sum-arr[index], index+1):
            return True

    return find_equal_subset_sum_recursive(arr, sum, index+1)

def find_subset_sum_recursive(arr, sum, index):
    return find_equal_subset_sum_recursive(arr, sum, 0)

def find_minimum_subset_sum(arr, sum1, sum2, index):
    if index == len(arr):
        return abs(sum1- sum2)

    diff1 = find_minimum_subset_sum(arr, sum1 + arr[index], sum2, index+1)

    diff2 = find_minimum_subset_sum(arr, sum1, sum2+arr[index], index+1)

    return min(diff1, diff2)


def count_subset_sum(arr, sum, index):
    if sum == 0:
        return 1
    if index >= len(arr):
        return 0

    sum1 = 0
    if arr[index] <= sum:
        sum1 = count_subset_sum(arr, sum-arr[index], index+1)

    sum2 = count_subset_sum(arr, sum, index+1)

    return sum1 + sum2

