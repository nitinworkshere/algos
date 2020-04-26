# Python 3 program to calculate
# the total fine collected

# function to calculate the total fine collected
def totFine(car_num, n, date, fine):
    tot_fine = 0

    # traverse the array elements
    for i in range(n):

        # if both car no and date are odd or
        # both are even, then statement
        # evaluates to true
        if (((car_num[i] ^ date) & 1) == 1):
            tot_fine += fine

        # required total fine
    return tot_fine


# Driver Program
if __name__ == "__main__":
    car_num = [3, 4, 1, 2]
    n = len(car_num)
    date, fine = 15, 250

    # function calling
    print(totFine(car_num, n, date, fine))

# This code is contributed by ANKITRAI1
