# A

list1 = [5, 10, 15, 20, 25, 50, 20]

#for i in range(len(list1)):
#    if list1[i] == 20:
#        list1[i] = 200
#        break
#print(list1)

index = list1.index(20)
list1[index] = 200
print(list1)

# B

aTuple = (10,20,30,40)
(a,b,c,d) = aTuple

print(aTuple)
print(a)
print(b)
print(c)
print(d)

# C

tuple1 = (11, 22, 33, 44, 55, 66)
var1 = tuple1.index(44)
var2 = tuple1.index(55)

result = (tuple1[var1],tuple1[var2])
print(result)

# D

tuple2 = (11, [22, 33], 44, 55)

for itera in range(len(tuple2)):
    if type(tuple2[itera]) == list:
        for iter2 in range(len(tuple2[itera])):
            if tuple2[itera][iter2] == 22:
                tuple2[itera][iter2] = 222

print(tuple2)


# E
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dic = dict(zip(keys, values))
print(dic)



