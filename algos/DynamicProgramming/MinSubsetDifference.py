def min_subset_difference(arr1, sum1, sum2):
    if sum1 == sum2:
        return 0

    if len(arr1) == 0:
        return sum2 - sum1

    diff1 = min_subset_difference(arr1[1:], sum1, sum2-arr1[0])
    diff2 = min_subset_difference(arr1[1:], sum1, sum2)

    return min(diff1, diff2)