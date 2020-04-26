def groupAnagrams(strs):
    d = {}
    ans = []
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in d:
            d[sorted_word] = [word]
        else:
            d[sorted_word].append(word)

    for key in d:
        ans.append(d[key])

    return ans

def groupAnagramsUsingMap(strs):
    d = {}
    for str in strs:
        if d.__contains__(str_encode(str)):
            d[str_encode(str)].append(str)
        else:
            d[str_encode(str)] = [str]
    for groups in d.values():
        print(groups)



def str_encode(pat):
    chars = [0]*26
    for ch in pat:
        index = ord(ch) - ord('a')
        if chars[index]:
            chars[index] += 1
        else:
            chars[index] = 1
    return str(chars)

print(groupAnagramsUsingMap(['dog', 'cat', 'god', 'tac']))
