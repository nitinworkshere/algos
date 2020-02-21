class Factorial:
    @staticmethod
    def calculatefactorial(number):
        if number == 1:
            return 1
        return number * Factorial.calculatefactorial(number - 1)