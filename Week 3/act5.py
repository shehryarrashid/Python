
# a

list_prime = [1]
user = int(input("Enter your limit number:"))
prime = True
for i in range(2,user+1):
    for j in range(2,i):
        if i % j == 0:
            prime = False
    if(prime):
        list_prime.append(i)
    prime = True
print(list_prime)

# b
year = int(input("Enter a year: "))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print(year, " is a leap year")
        else:
            print(year, " is not a leap year")
    else:
        print(year, " is a leap year")
else:
    print(year, " is not a leap year")
