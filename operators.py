"""
program to demonstrate operators
"""
i=int(input("Enter the first operand "))
a=int(input("Enter the second operand "))

c=i+a
print ("sum of {} and {} is {}".format(i, a, c))

c=i-a
print ("difference of {} and {} is {}".format(i, a, c))

c=i/a
print ("quotient of {} and {} is {}".format(i, a, c))

c=i*a
print ("product of {} and {} is {}".format(i, a, c))

c=i//a
print ("floor of {} and {} is {}".format(i, a, c))
