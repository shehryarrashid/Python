
# A
sampleList = [10, 20, 30, 40, 50]
sampleList.append(60)
print(sampleList)
sampleList.append(60)
print(sampleList)
# Output: [10, 20, 30, 40, 50, 60, 60]

# B

aList = [100, 200, 300, 400, 500]
aTuple = (10, 20, 30, 40, 50)

aList.reverse()
print(tuple(reversed(aTuple)))
print(aList)

# C
aList = [1, 2, 3, 4, 5, 6, 7]
for i in range(len(aList)):
    aList[i] **= 2
print(aList)

# D

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

solution = tuple(zip(list1,reversed(list2)))
print(solution)

# E

def max_list(lista):
    biggest = lista[0]
    for i in range(1, len(lista)):
        if biggest < lista[i]:
            biggest = lista[i]
    return biggest


def smallest(lista):
    small = lista[0]
    for i in range(1, len(lista)):
        if small > lista[i]:
            small = lista[i]
    return small

print("The maximum is: ", max_list(list1))
print("The smallest is: ", smallest(list1))










