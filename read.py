file = open("main.txt", "r")

print(file.read())

print(file.readline())


for x in file:
    print(x)