from math import inf

def max_ribbon_cut(lengths, length, index=0):
    if index >= len(lengths):
        return -inf

    if length == 0:
        return 0

    count1 = -inf
    if lengths[index] <= length:
        local_count = max_ribbon_cut(lengths, length-lengths[index], index)
        if local_count != -inf:
            count1 = local_count + 1

    count2 = max_ribbon_cut(lengths, length, index+1)
    return max(count1, count2)
