#Define a function

def multiplyFunc(x):
    result = x * x
    return result

print(multiplyFunc(5))

#Call the function

print(multiplyFunc(6))
print(multiplyFunc(3))

#Anonymous Lambda

def new(i):
    return lambda x: x * i

double = new(2)
triple = new(3)

print(double(5))
print(triple(5))