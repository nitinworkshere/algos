def printOccurances(string):
    result = ''
    index = 1
    next_non_duplicate_index = 1
    frequency_counter = 1
    while index < len(string):
        if string[next_non_duplicate_index-1] != string[index]:
            print(string[next_non_duplicate_index-1],string[index])
            next_non_duplicate_index = index
            str1 = string[next_non_duplicate_index-1]+str(frequency_counter)
            result += str1
            frequency_counter = 1

        print('came with '+string[index] + str(frequency_counter))
        frequency_counter += 1
        index += 1
    return result


print(printOccurances('aaabbbcd'))
