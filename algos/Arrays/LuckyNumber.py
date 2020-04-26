# Returns 1 if n is a lucky number otherwise returns 0
counter = 1
def isLucky(n):
    global counter
    # Function attribute will act as static variable

    # just for readability, can be removed and used n instead
    next_position = n

    if counter > n:
        return 1
    if n % counter == 0:
        return 0

    # Calculate next position of input number
    next_position = next_position - next_position / counter

    counter += 1

    return isLucky(next_position)



print(isLucky(11))