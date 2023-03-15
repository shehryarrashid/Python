# a
for i in range(1,7):
    if i == 3 or i == 6:
        continue
    else:
        print(i)

# b

numbers = (1,2,3,4,5,6,7,8,9)
odd,even = 0,0
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Number of odds: " + str(odd) + "\nEvens: " + str(even))

# c

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

for item in datalist:
    print(type(item))