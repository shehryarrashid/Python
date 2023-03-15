
# Shehryar Rashid 
# Activity 4 Part 1 a)

print("This program tells you the greater number between 2 numbers")
a = int(input("Enter a number:"))
b = int(input("Enter another number: "))

if(a > b):
    print("The bigger number is: "+ str(a))
elif(a == b):
    print("Both numbers are same")
else:
    print("The bigger number is: " + str(b))


# Part 2 b) 

print(" Welcome to newton E=mc2 calculator")

mass = int(input("Enter a Mass: ")) 
c = 3 * 10**8 # Velocity of speed
energy = mass * c # Using the equation

print("The energy result for the mass" + str(mass) + " is: " + str(energy))

# Part 3 c) 

print("-------------------Welcome to an odd and even calculator---------------------------")

num1 = int(input("Enter a number: "))
if(num1 % 2 == 0):
    print("You have entered a even number")
    print("The square of " + str(num1) + " is " + str(num1**2))
else:
    print("You have entered an odd number")
    print("The cude of" + str(num1) + " is " + str(num1**3))
    






