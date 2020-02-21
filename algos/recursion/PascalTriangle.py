class PascalTriangle:
    def __init__(self, height):
        self.height = height

    def printoutput(self):
        for i in range[self.height, 0, -1]:
            print(PascalTriangle(i, self.height- i))


    @staticmethod
    def calculatepascalsum(row, col):
        if row == 0:
            return 1
        if col < 0:
            return 0
        return PascalTriangle.calculatepascalsum(row-1, col-1) + PascalTriangle.calculatepascalsum(row-1, col)


