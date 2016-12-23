"""
wap to get x and y coordinates from the user and print which quadrant it is in.
"""

x = int(input("Enter x coordinate "))
y = int(input("Enter y coordinate "))

print ("(x,y) = ({0}, {1})".format(x,y))

if ((x > 0) and (y > 0)):
    print ("Coordinate in Quadrant 1")
elif ((x > 0) and (y < 0)):
    print ("Coordinate in Quadrant 4")
elif ((x < 0) and (y > 0)):
    print ("Coordinate in Quadrant 2")
else:
    print ("Coordinate in Quadrant 3")