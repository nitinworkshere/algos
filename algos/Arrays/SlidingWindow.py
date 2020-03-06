def subarray_k_size_with_sum(arr, k):
    global_max_sum = 0
    for i in range(len(arr) -k +1):
        window_sum = 0
        for j in range(i, k+i):
            window_sum += arr[j]
        global_max_sum = max(global_max_sum, window_sum)
    return global_max_sum

#with each slide remove the element being kicked out and include the element being included
def subarray_k_size_with_sum_better_approach(arr, k):
    window_start = 0
    window_sum, global_sum = 0, 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k-1: #window size reached
            global_sum = max(global_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return global_sum



