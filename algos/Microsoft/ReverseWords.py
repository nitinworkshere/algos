# Python3 implementation of the approach

# Function to resturn the after
# reversing the individual words
def reverseWords(Str):
    # Pointer to the first character
    # of the first word

    start = 0
    for i in range(len(Str)):
        # If the current word has ended
        if (Str[i] == ' ' or i == len(Str) - 1):

            # Pointer to the last character
            # of the current word
            end = i - 1
            if (i == len(Str) - 1):
                end = i

            # Reverse the current word
            while (start < end):
                Str[start], Str[end] = Str[end], Str[start]
                start += 1
                end -= 1

            # Pointer to the first character
            # of the next word
            start = i + 1

    return "".join(Str)


# Driver code
Str = "Geeks for Geeks"
Str = [i for i in Str]

print(reverseWords(Str))

# This code is contributed by mohit kumar 29
