def romanToInt(self, s: str) -> int:
    look_up = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    res = 0
    index = 0
    while index < len(s):
        next_index = index + 1
        if next_index < len(s) and look_up.get(s[next_index]) > look_up.get(s[index]):
            res = res + (look_up.get(s[next_index]) - look_up.get(s[index]))
            index = next_index + 1
        else:
            res = res + look_up.get(s[index])
            index = index + 1
    return res
