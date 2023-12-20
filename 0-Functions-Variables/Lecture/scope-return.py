# Scope and Return Values

# In the following, name will return an error as it is being called in a function before it has been defined
# def main():
#     name = input("What's your name? ")
#     hello()


# def hello():
#     print("hello,", name)


# main()


# The folowing works better
# def main():
#     name = input("What's your name? ")
#     hello(name)


# def hello(to="world"):
#     print("hello,", to)


# main()


# Return
def main():
    x = int(input("What's x? "))

    print("x squared is", square(x))


def square(n):
    return n * n
    # return n ** 2
    # return pow(n, 2)


main()
