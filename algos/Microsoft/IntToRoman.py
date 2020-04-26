def intToRoman(self, num):

    romans = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    result = ""
    d = 1
    while num > 0:
        n = num % 10
        result = self.get_sub_num(n, d, romans) + result
        num /= 10
        d *= 10
    return result


def get_sub_num(self, n, d, romans):
    if n  <= 3:
        return "".join([romans[1*d] for _ in range(n)])
    elif n == 4:
        return romans[1*d] + romans[5*d]
    elif n <= 8:
        return romans[5*d] + "".join([romans[1*d] for _ in range(n-5)])
    else: # n == 9
        return romans[1*d]  + romans[10*d]


d = {1000: "M",
     900: "CM", 500: "D", 400: "CD", 100: "C", 200: "CC", 300: "CCC", 600: "DC", 700: "DCC", 800: "DCCC",
     90: "XC", 50: "L", 40: "XL", 10: "X", 20: "XX", 30: "XXX",  60: "LX", 70: "LXX", 80: "LXXX",
     9: "IX", 5: "V", 4: "IV", 1: "I", 2: "II", 3: "III", 6: "VI", 7: "VII", 8: "VIII",  0: ""}
def int_to_roman(num):
    return d[(num // 1000) * 1000] + d[((num % 1000) // 100) * 100] + d[((num % 100) // 10) * 10] + d[(num % 10)]

