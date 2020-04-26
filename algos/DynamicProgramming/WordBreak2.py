def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    self.memo = {}
    return [" ".join(i) for i in self.helper(s, 0, len(s), set(wordDict))]


def helper(self, s, start, n, dict_set):
    if start == n:
        return [[]]
    if start in self.memo:
        return self.memo[start]
    res = []
    for i in range(start, n):
        if s[start: i + 1] in dict_set:
            for part in self.helper(s, i + 1, n, dict_set):
                res.append([s[start: i + 1]] + part)
    self.memo[start] = res
    return res