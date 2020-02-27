def longest_common_substr(str1, str2):
    return longest_common_substr_rec(str1, str2, 0, 0, 0)


def longest_common_substr_rec(str1, str2, index1, index2, count):
    if index1 == len(str1) or index2 == len(str2):
        return count
    if str1[index1] == str2[index2]:
        count = longest_common_substr_rec(str1, str2, index1+1, index2+1, count+1)

    c1 = longest_common_substr_rec(str1, str2, index1 + 1, index2, 0)
    c2 = longest_common_substr_rec(str1, str2, index1, index2+1, 0)

    return max(count, max(c1, c2))
