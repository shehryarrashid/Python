# Shehryar Rashid 
# Week 2 Activity one
print("wELCOME TO NUMBER SWAP")
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
# Now the swap happens
aux = a # auxiliar variable
a = b
b = aux
# print swap result
print("Now a is: " + str(a) + " and b is: " + str(b))

# ACtivity 2 b)
a,b = b,a
print("Values swapped again.")
print("Now a is: " + str(a) + " and b is: " + str(b))

