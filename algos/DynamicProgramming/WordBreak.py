#complexity O(2^n)
def word_break_rec(s, dict={}):
    if s == '':
        return True
    for i in range(1, len(s)+1):
        if dict[s[i]] and word_break_rec(s[i+1:]):
            return True
    else:
        False

