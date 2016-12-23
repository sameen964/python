"""
wap to accept a number 'n' 
waf to print 1 to n
"""

n = int(input("Enter value for 'n' "))

def printN(n):
    i = 0
    while (i < n):
        i = i + 1
        print (i)

printN(n)
