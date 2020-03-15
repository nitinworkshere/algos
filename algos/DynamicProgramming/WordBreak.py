#complexity O(2^n)
def word_break_rec(s, dict={}):
    if s == '':
        return True
    for i in range(1, len(s)+1):
        if dict.__contains__(s[0:i]) and word_break_rec(s[i:], dict):
            return True
    else:
        return False


s, wordDict = "ilikesamsung", {"i", "like","sung"}

print(word_break_rec(s, wordDict))
