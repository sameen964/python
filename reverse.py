"""
program to reverse a number
waf called reverse which accepts a number and returns the reverse of it
"""
import time 

def reverse(num):
    """
    num1 = num%10
    num2 = num//10
    num3 = num2%10
    num4 = num2//10
    num5 = num4%10

    rev = (num1 * 100) + (num3 * 10) + (num5)
    """

    rev = 0
    digit = 0

    print("before loop")
    print (digit, num, rev)

    print("while loop")
    while(num > 0):
         digit = num%10
         num = num//10
         rev = (rev * 10) + digit
         print (digit, num, rev)
         time.sleep(4)

    print("after loop")
    print (digit, num, rev)

    return rev     


num = int(input("enter a number: "))

print ("The reverse of {} is: {}".format(num,reverse(num)))