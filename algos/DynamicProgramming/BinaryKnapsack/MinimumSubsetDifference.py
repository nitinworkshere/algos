def minimum_subset_difference(arr, sum1=0, sum2=0, index=0):
    if index == len(arr):
        return abs(sum1 - sum2)

    diff1 = minimum_subset_difference(arr, sum1 + arr[index], sum2, index+1)
    diff2 = minimum_subset_difference(arr, sum1, sum2 + arr[index], index+1)

    return min(diff1, diff2)

print(minimum_subset_difference([1, 3, 100, 4]))