"""
@author Ananda This is another very common program to practice loop and
 *         condition statement This program will validate whether a given number
 *         is Prime or not A prime number is a number which is not divisible by
 *         any other number, e.g. 3, 5, 7, 11, 13, 17,
 """


def checkIfPrime(num):

    count = 0
    if num < 2:
        print("This is an invalid number.")
    else:
        for i in range(1, num+1):
            if num % i == 0:
                count = count+1
        if count == 2:
            print("The number: ", num, " is a Prime number")
        else:
            print("The number: ", num, " is not a Prime number")


num = int(input("Enter a number to check whether Prime or not: \t "))
checkIfPrime(num)