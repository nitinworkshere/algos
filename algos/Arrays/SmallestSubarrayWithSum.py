from math import inf
def smallest_subarray_with_sum(arr, sum):
    window_sum = 0
    min_length = inf
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        while window_sum >= sum:
            min_length = min(min_length, window_end-window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1

        if min_length == inf:
            return 0

        return min_length   