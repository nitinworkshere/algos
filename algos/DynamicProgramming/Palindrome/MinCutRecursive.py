def find_MPP_cuts_recursive(st, startIndex, endIndex):
    # we don't need to cut the string if it is a palindrome
    if startIndex >= endIndex or is_palindrome(st, startIndex, endIndex):
        return 0

    # at max, we need to cut the string into its 'length-1' pieces
    minimumCuts = endIndex - startIndex
    for i in range(startIndex, endIndex + 1):
        if is_palindrome(st, startIndex, i):
            # we can cut here as we have a palindrome from 'startIndex' to 'i'
            minimumCuts = min(
                minimumCuts, 1 + find_MPP_cuts_recursive(st, i + 1, endIndex))

    return minimumCuts


def is_palindrome(st, x, y):
  while (x < y):
    if st[x] != st[y]:
      return False
    x += 1
    y -= 1
  return True
