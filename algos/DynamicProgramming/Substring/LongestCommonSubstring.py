def longest_common_substring(st1, st2, index1=0, index2=0, count=0):

    if index1 >= len(st1) or index2 >= len(st2):
        return count

    if st1[index1] == st2[index2]:
        count = longest_common_substring(st1, st2, index1+1, index2+1, count+1)

    c1 = longest_common_substring(st1, st2, index1+1, index2, 0)
    c2 = longest_common_substring(st1, st2, index1, index2+1, 0)

    return max(count, max(c1, c2))

