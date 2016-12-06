"""
Program to test control flow.
"""

"""
Control block to get name and age of a person and tell whether the person is allowed to view content or not.
"""

name = input("Enter name ")
age = int(input("Enter age "))

print ("Hello {}, you are {} years old".format(name, age))

if (age >= 21):
	print ("You are allowed to enter {}".format(name))
else:
	print ("You are not old enough to enter {}".format(name))

"""
Control block to check age and list permittable movie ratings
"""

if (age <= 13):
	print ("You're allowed to watch movies with the following ratings: \
G, PG, PG-13, {}".format(name))
elif (age > 13 and age < 17):
	print ("You're allowed to watch movies with the following ratings: \
G, PG, PG-13, R (with guardian)".format(name))
else:
	print ("You're allowed to watch movies with the following ratings: \
G, PG, PG-13, R, NC-17, {}".format(name))

"""
Control block to check age and list movies that are not permittable.
"""