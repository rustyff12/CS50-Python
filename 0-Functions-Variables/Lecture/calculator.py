# Integers and Operators
# Interactive mode is just 'python' in terminal
# no upper bounds on "int" in python but there is to "float"

# Calcuator
# needs int() otherwise it concatenates
# x = input("What's x? ")
# y = input("What's y? ")
# print(int(x) + int(y))

# x = int(input("What's x? "))
# y = int(input("What's y? "))

# Also possible
# print(int(input("What's x? ")) + int(input("What's y? ")))

# x = int(input("What's x? "))
# y = int(input("What's y? "))

# print(x + y)

# Float = floating point or decimal value
# x = float(input("What's x? "))
# y = float(input("What's y? "))

# print(x + y)

# Rounding
# [, ndigits] means it is optional
# round(number[, ndigits])

# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z = round(x + y)
# print(f"{z:,}")
# prints 1,000 rather than 1000


x = float(input("What's x? "))
y = float(input("What's y? "))

# rounds to 2 digits
z = round(x / y, 2)
# print(z)

# f string approach
print(f"{z:.2f}")
