"""
 * @author Ananda
 This is one of the very common program in all languages.
 Fibonacci numbers are used to create technical indicators using a mathematical sequence
 developed by the Italian mathematician, commonly referred to as "Fibonacci,"
 For example, the early part of the sequence is 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,144, 233, 377, and so on

 This program will calculate and print first "N" Fibonacci number where "N" will be input by user
 """

def calculateFibonacci(num):
    fibo1 = 0
    fibonacci = 0
    fibo2 = 1

    print("Fibonacci series upto ", num, " is as follows:")

    if num == 1:
        print(0)
    elif num == 2:
        print(1)
    else:
        print(fibo1, "\t", fibo1, end="\t")
        for i in range(3, num + 1):
            #Fibonacci number is sum of previous two Fibonacci number
            fibonacci = fibo1 + fibo2
            fibo1 = fibo2
            fibo2 = fibonacci
            print(fibonacci, end="\t")


num = int(input("Enter number upto which Fibonacci series to print: "))
calculateFibonacci(num)
