# accessing list values
list1 = ['physics','chemistry',1997, 2000]
list2 = [1,2,3,4,5,6,7]

print("list1[0]: ",list1[0])
print("list2[1:5]",list2[1:5])


# updating list values

list = ['physics','chemistry',1997,2000]
list = ['physics', 'chemistry', 1997, 2000];
print ("Value available at index 2 : ")
print (list[2])
list[2] = 2001;
print ("New value available at index 2 : ")
print (list[2])
print (list)

# Python program to demonstrate
# Addition of elements in a List

# Creating a list

List = []
print("initial blank list:")
print(List)

# Addition of elements in the list

List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of the three elements:")
print(List)

# Adding elements through an iterator:

for i in range(1,4):
    List.append(i)
print("\n List of elements")
print(List)

# Adding a touple to the list
List.append((5,6))
print(List)

# Insert method

List.insert(3,"Shehryar")
print(List)


# Dictionary

Dict = {1:"My Name is",2:"Khan", 3:"And Im Muslim"}
print(Dict)

































