#opposite of min coin change
from math import inf
def max_ribbon_cut(lengths, length, current_index=0):
    if length == 0:
        return 0

    if current_index >= len(lengths):
        return -inf

    count1 = -inf
    if lengths[current_index] <= length:
        result = max_ribbon_cut(lengths, length-lengths[current_index], current_index)
        if result != -inf:
            count1 = result + 1
    count2 = max_ribbon_cut(lengths, length, current_index+1)
    return max(count1, count2)