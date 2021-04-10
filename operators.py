#comparison operator example
x = 2
y = 4

print(x <= y)

#logical operators

print(x < 3 and x < 5)
print(not(x < 3 and y > 2))

#additional operators
list1 = ["Barcelona", "Madrid"]
list2 = ["Barcelona", "Madrid"]
list3 = list2

print(list1 is list2) #false bc the value of list1 and 2 are the same but they are different objects in diff locations
print(list2 is list3) #true
print("Barcelona" in list3)