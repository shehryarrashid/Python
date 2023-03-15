# Activity 1 Shehryar Rashid
# Week 2 Activity 1
from cmath import pi
import math
x = 5
y = 2 
x += 5 # Added Later On
y *= 2 # "
# Arithm,etic Operations
#print(x - y) # 3
#print(x * y) # 10
#print(x / y) # 2.5
#print(x % y) # 1 
#print(x // y) # 2
#print(x ** y) # 25
# Boolean Statements
#print(x >= y) # True
#print(x != y) # True
#print(x <= 10 and not(y==2)) # False
#print(x is not y) # True
#print(1 + int('2')) # 3
#print(str(1) + '2') # 12

# Part 2 b)

print("----------------------------Welcome to regular rectangle area calculator---------------- ")
h = int(input("Enter the height: "))
b = int(input("Enter base length: "))
area = h * b 
print("The area of the rectagle is : " + str(area))

# Part 3 c)

print("----------------------------Welcome to regular circle area calculator---------------- ")
radius = float(input("Enter circle radius: "))
area_c = radius**2 * math.pi
print("The area of circle with radius " + str(radius) + " is: " + str(area_c)) 
