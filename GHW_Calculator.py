import math
 
print("Welcome to Global Human Wealth Calculator!")

def add (x1, x2):
    return x1 + x2

def sub (x1, x2):
    return x1 - x2

def multiply (x1, x2):
    return x1 * x2

def divide (x1, x2):
    return x1 / x2

options = [ add, sub, multiply, divide]

print(options)

select = input("Select option: ")

x1 = float(input("Enter value: "))
x2 = float(input("Enter value: "))

if add == select:
    print(x1, "+", x2, "=",
                    add(x1, x2))


elif sub == select:
     print(x1, "-", x2, "=",
                    sub(x1, x2))


elif multiply == select:
     print(x1, "*", x2, "=",
                    multiply(x1, x2))


elif divide == select:
     print(x1, "/", x2, "=",
                    divide(x1, x2))

else:
    list()
