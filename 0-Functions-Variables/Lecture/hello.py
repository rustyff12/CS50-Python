# Arguments/Parameters - an input to a function that somehow influences it's behaviour
# print("Hello, world")


# input("What's your name? ")
# print("Hello, world")

# variables - variable is a container for some value
# "=" is the assingment operator

# Ask user for their name
name = input("What's your name? ")
# print("Hello, " + name)
# What's your name? input =>
# Russell
# second option doesn't need extra space
# print("Hello,", name)


print("Hello, ", end="")
print(name)

print("Hello, ", name, sep="???")
# print("Hello, "friend"") won't work, need single and double quotes
print('Hello, "friend"')
print('Hello, "friend"')  # Escaping characters works like JavaScript
