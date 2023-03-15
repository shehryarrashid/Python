# Shehryar Rashid 
# Activity 5 Part 1 a) 
print("string to float:", float("3.4"))
print("float to int:", int(3.4))
#print("fractional string to int:", int("3.4")) comment this line so program runs
# int() converts float values to int or an integer string into a integer
# Does what mentioned in the line before
# It gives error

# Part 2 b)
first = 1.0
second = "1"
third = "1.1"

print(first + float(second)) # 2.0
print(float(second) + float(third)) # 2.1
#print(first + int(third)) error
print(first + int(float(third))) # 2.0
print(int(first) + int(float(third))) # 2
#print(2.0 * second) error

# Part 3 c)
gross_world_product = 84.84
gwp_str = str(gross_world_product) # Just cast str()
answer_8 = "In 2018 gross product of the world (GWP) was " + gwp_str + " in trillion US dollars."
print(answer_8)