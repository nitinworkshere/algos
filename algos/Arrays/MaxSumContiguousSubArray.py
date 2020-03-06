#this algorithm uses kadane's algo A = [-2, 1, -3, 4, -1, 2, 1, -5, 1]


def max_sum_sub_array(arr):
    local_max = 0
    max_over_all = 0
    start, end = 0, 0
    for i in range(len(arr)):
        local_max += arr[i]
        if local_max < 0:
            local_max = 0
            start = i + 1
            end = start
        if max_over_all < local_max:
            max_over_all = local_max
            end = i
    print(start, end)


max_sum_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 7])

