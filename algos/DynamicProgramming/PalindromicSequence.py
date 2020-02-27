def longest_palindromic_subseq(str):
    return longest_palindromic_subseq_rec(str, 0, len(str)-1)


def longest_palindromic_subseq_rec(str, start, end):
    if start > end:
        return 0
    if start == end:
        return 1

    if str[start] == str[end]:
        return 2 + longest_palindromic_subseq_rec(str, start+1, end-1)

    c1 = longest_palindromic_subseq_rec(str, start+1, end)
    c2 = longest_palindromic_subseq_rec(str, start, end-1)

    return max(c1, c2)

