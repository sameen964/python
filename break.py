"""
Program to check length of string; break statement
"""

while True:

    s = input("Enter something: ")
    if (s == "quit"):
        break

    print ("length of string is ", len(s))

print ("done")