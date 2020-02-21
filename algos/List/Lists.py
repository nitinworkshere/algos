class Lists:

    @staticmethod
    def rotatelistbyn(lst, n):
        pivot = len(lst) - n
        result = lst[pivot:]

        for i in range(0, pivot - 1):
            result.append(lst[i])

        return result