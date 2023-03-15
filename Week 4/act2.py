
# A
def showEmployee(name,salary = 9000):
    print("Name: " + str(name) + " Salary: " + str(salary))

#showEmployee("Ben",12000)
#showEmployee("Jessa")
# B
def func1(*values):
    for item in values:
        print("New item:" + str(item))
#func1("phone","tv","champion",13)
# C
def max(a,b):
    if a >= b:
        return a
    else:
        return b
#D
def numbers(lista):
    sum = 0
    for item in lista:
        sum = sum + item
    return sum
#List = [8, 2, 3, 0, 7]
#print(numbers(List))