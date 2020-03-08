def longest_common_subsequence(st1, st2, index1=0, index2=0):

    if index1 >= len(st1) or index2 >= len(st2):
        return 0

    if st1[index1] == st2[index2]:
        return 1 + longest_common_subsequence(st1, st2, index1+1, index2+1)

    c1 = longest_common_subsequence(st1, st2, index1+1, index2)
    c2 = longest_common_subsequence(st1, st2, index1, index2+1)

    return max(c1, c2)