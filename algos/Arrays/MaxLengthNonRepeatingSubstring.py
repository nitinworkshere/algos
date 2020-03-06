def max_length_non_repeating_substr(string):
    window_start = 0
    max_length = 0
    char_index_map = {}

    for window_end in range(len(string)):
        right_char = string[window_end]
        if char_index_map[right_char]:
            # set start to where right char index was set
            window_start = max(window_start, char_index_map[right_char]+1)

        char_index_map[right_char] = window_end
        max_length = max(max_length, window_end - window_start + 1)
    return max_length
