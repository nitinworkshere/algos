#complexity O(2^n)
def word_break_rec(s, dict={}):
    if s == '':
        return True
    for i in range(1, len(s)+1):
        if dict.__contains__(s[0:i]) and word_break_rec(s[i:], dict):
            return True
    else:
        return False


def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    arr = [0] * len(s)
    for i in range(len(s)):
        for j in range(i - 1, -1, -1):
            if arr[j] == 1 and s[j + 1:i + 1] in wordDict:
                arr[i] = 1
                break
        else:
            if s[:i + 1] in wordDict:
                arr[i] = 1
    return arr[len(s) - 1] == 1


s, wordDict = "ilikesamsung", {"i", "like","sung"}



print(word_break_rec(s, wordDict))
