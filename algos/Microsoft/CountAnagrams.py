def findAnagrams(self, s: str, p: str) -> List[int]:
    p_sorted = sorted(p)
    n_s = len(s)
    n_p = len(p)
    res = []
    for i in range(n_s - n_p + 1):
        if sorted(s[i:i + n_p]) == p_sorted:
            res.append(i)
    return res
