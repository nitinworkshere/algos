def find_max_steal(wealths, curr_index = 0):
    if curr_index >= len(wealths):
        return 0
    steal_current = wealths[curr_index] + find_max_steal(wealths, curr_index+2)
    skip_current = find_max_steal(curr_index+1)

    return max(steal_current, skip_current)