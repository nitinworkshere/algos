# Python3 program to find difficulty
# of a sentence

# Utility function to check character
# is vowel or not
def isVowel(ch):
    return (ch == 'a' or ch == 'e' or
            ch == 'i' or ch == 'o' or
            ch == 'u')


# Function to calculate difficulty
def calcDiff(str):
    str = str.lower()
    count_vowels = 0
    count_conso = 0
    consec_conso = 0
    hard_words = 0
    easy_words = 0

    # Start traversing the string
    for i in range(0, len(str)):

        # Check if current character is
        # vowel or consonant
        if (str[i] != " " and isVowel(str[i])):

            # Increment if vowel
            count_vowels += 1
            consec_conso = 0

        # Increment counter for consonant
        # also mainatin a separate counter for
        # counting consecutive consonants
        elif (str[i] != " "):
            count_conso += 1
            consec_conso += 1

        # If we get 4 consecutive consonants
        # then it is a hard word
        if (consec_conso == 4):
            hrad_words += 1

            # Move to the next word
            while (i < len(str) and str[i] != " "):
                i += 1

            # Reset all counts
            count_conso = 0
            count_vowels = 0
            consec_conso = 0
        elif (i < len(str) and (str[i] == ' ' or
                                i == len(str) - 1)):

            # Increment hard_words, if no. of
            # consonants are higher than no. of
            # vowels, otherwise increment count_vowels
            if (count_conso > count_vowels):
                hard_words += 1
            else:
                easy_words += 1

            # Reset all counts
            count_conso = 0
            count_vowels = 0
            consec_conso = 0

    # Return difficulty of sentence
    return (5 * hard_words + 3 * easy_words)


# Driver Code
if __name__ == "__main__":
    str = "I am a geek"
    str2 = "We are geeks"
    print(calcDiff(str))
    print(calcDiff(str2))

# This code is contributed
# by Sairahul Jella
