#kadane's algorithm
def find_max_sub_array(arr):
    max_so_far = 0
    max_overall = 0
    start, end, s = 0, 0, 0

    for i in range(len(arr)):
        max_so_far += arr[i]
        if max_so_far < 0: #Now total is getting less than 0
            max_so_far = 0
            s = i+1 #only reset start when 0 occured

        if max_so_far > max_overall:
            max_overall = max_so_far
            start = s
            end = i
    return max_overall
