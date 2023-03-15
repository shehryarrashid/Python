# prints a triangle
def part_a():
    for i in range(1,6):
        for j in range(1,i+1):
            print(j , end = " ")
        print()

# Checks for prime numbers
def part_b():
    prime = []
    ok = True
    for num in range(25,51):
        for var in range(2,num):
            if(num % var == 0):
                ok = False
        if(ok):
            prime.append(num)
        ok = True
    return prime

print(part_b())

