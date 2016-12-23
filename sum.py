"""
Function to get two numbers from the user,  compute and print the sum

def sum():
    num1 = int(input("Enter first number "))
    num2 = int(input("Enter second number "))
    sum = num1 + num2
    print("{2} is the sum of {0} and {1}".format(num1, num2, sum))
sum()

"""


"""
Program to get two numbers from user, and pass to function
Function to accept two numbers ,  compute and print the sum
"""

def sum2(x, y):
    print(x + y)

num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))
sum2(num1, num2)
sum2(num1, 10)
sum2(10, num2)
sum2(10, 10)

"""
Program to get two numbers from user, and pass to function
Function to accept two numbers ,  compute the sum, return sum
"""

