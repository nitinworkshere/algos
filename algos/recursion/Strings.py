class Strings:
    @staticmethod
    def reversestringrecursive(str):
        if len(str) == 1:
            return str
        return Strings.reversestringrecursive(str[1:])+str[0]

    @staticmethod
    def reversestringiterative(str):
        reverse = ''
        length = len(str)-1
        while length >= 0:
            reverse = reverse + str[length]
            length = length - 1
        return reverse

    @staticmethod
    def countvowelrecurive(str):
        if len(str) == 0:
            return 0
        return Strings.countvowelrecurive(str[1:]) + Strings.isvowel(str[0])

    @staticmethod
    def countvoweliterative(str):
        count = 0
        length = len(str)-1
        while length >= 0:
            count = count + Strings.isvowel(str[length])
            length = length - 1
        return count



    @staticmethod
    def isvowel(char):
        return 1 if char in ['a', 'e', 'i', 'o', 'u'] else 0


    @staticmethod
    def removetabfromstring(str):
        if not str:
            return ""
        if str[0] == "\t" or str[0] == " ":
            return str[1:]
        else:
            return str[0]+Strings.removetabfromstring(str[1:])


    @staticmethod
    def removeadjduplicates(str):
        if not str:
            return ""
        if len(str) == 1:
            return str
        if str[0] == str[1]:
            return Strings.removetabfromstring(str[1:])
        else:
            return str[0]+Strings.removetabfromstring(str[1:])

    @staticmethod
    def mergetwosortedstring(str1, str2):
        if not str1:
            return str2
        if not str2:
            return str1
        if str1[0] > str2[0]:
            return str2[0]+Strings.mergetwosortedstring(str1, str2[1:])
        return str1[0]+Strings.mergetwosortedstring(str1[1:], str2)

    @staticmethod
    def lengthofstring(str):
        if not str:
            return 0
        return 1 + Strings.lengthofstring(str[1:])

    @staticmethod
    def checkpalindrome(str):
        if len(str) <= 1:
            return True
        if str[0] == str[len(str)-1]:
            Strings.checkpalindrome(str[1:len(str)-1])

        return False



