# Python program to remvoe duplicate characters from an
# input string
NO_OF_CHARS = 256


# Since strings in Python are immutable and cannot be changed
# This utility function will convert the string to list
def toMutable(string):
    List = []
    for i in string:
        List.append(i)
    return List


# Utility function that changes list to string
def toString(List):
    return ''.join(List)


# Function removes duplicate characters from the string
# This function work in-place and fills null characters
# in the extra space left
def removeDups(string):
    bin_hash = [0] * NO_OF_CHARS
    ip_ind = 0
    res_ind = 0
    temp = ''
    mutableString = toMutable(string)

    # In place removal of duplicate characters
    while ip_ind != len(mutableString):
        temp = mutableString[ip_ind]
        if bin_hash[ord(temp)] == 0:
            bin_hash[ord(temp)] = 1
            mutableString[res_ind] = mutableString[ip_ind]
            res_ind += 1
        ip_ind += 1

    # After above step string is stringiittg.
    # Removing extra iittg after string
    return toString(mutableString[0:res_ind])

#https://www.geeksforgeeks.org/remove-duplicates-from-a-string-in-o1-extra-space/
# Python3 implementation of above approach

# Function to remove duplicates
def removeDuplicatesFromString(str2):
    # keeps track of visited characters
    counter = 0;

    i = 0;
    size = len(str2);
    str1 = list(str2);

    # gets character value
    x = 0;

    # keeps track of length of resultant string
    length = 0;

    while (i < size):
        x = ord(str1[i]) - 97

        # check if Xth bit of counter is unset
        if ((counter & (1 << x)) == 0):
            str1[length] = chr(97 + x)

            # mark current character as visited
            counter = counter | (1 << x)

            length += 1
        i += 1

    str2 = ''.join(str1);
    return str2[0:length];


# Driver code
str1 = "geeksforgeeks";
print(removeDuplicatesFromString(str1));

# This code is contributed by mits


# Driver program to test the above functions
string = "geeksforgeeks"
print
removeDups(string)

# A shorter version for this program is as follows
# import collections
# print ''.join(collections.OrderedDict.fromkeys(string))

# This code is contributed by Bhavya Jain
