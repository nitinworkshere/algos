def generateParenthesis(n: int):
    return generate("", n, n)

    # s:current result, l:remaining left parentheses, r:remainling right parentheses


def generate(s: str, l: int, r: int):
    if l == 0 and r == 0: return [s]
    left = generate(s + "(", l - 1, r) if l > 0 else []  # add (
    right = generate(s + ")", l, r - 1) if r > l else []  # add )
    return left + right


print(generateParenthesis(3))