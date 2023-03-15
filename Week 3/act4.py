
# a
num1 = 0
num2 = 1
fibo = 0
for i in range(50):
    print(fibo, end=" ")
    num1 = num2
    num2 = fibo
    fibo = num1 + num2


# b

for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# c
user = input("Enter anything you want: ")
dig,alpha = 0,0
for lett in user:
    if lett.isdigit():
        dig += 1
    if lett.isalpha():
        alpha += 1
print("Digits: " + str(dig) + "\nLetters: " + str(alpha))


