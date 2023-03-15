# A

def recursive(num):
    if num == 0:
        return 0
    else:
        return num + recursive(num - 1)

print(recursive(10))


# B

def power(a, b):
    if b == 0:
        return 1
    else:
        b -= 1
        return a * power(a,b)

print(power(2,10))

