def dict_pattern_match(pat, dict):
    arr = []
    for word in dict:
        if len(word) == len(pat) and encode(pat) == encode(word):
            arr.append(word)
    return arr




def encode(pat):
    patternMap = {}
    hash = ''
    i=0
    for index in range(len(pat)):
        if not patternMap.__contains__(pat[index]):
            patternMap[pat[index]] = i
            i += 1
        hash += str(patternMap[pat[index]])
    return hash





pat = "foo"
dict = {"New", "Too", "Abb"}
print(dict_pattern_match(pat, dict))