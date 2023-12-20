# Functions

# Ask user for their name
# name = input("Whats's your name?").strip().title()

# Say hello to user
# print(f"Hello, {name}")


# def hello():
#     name = input("What's your name? ")

#     print(name)


# hello()
# def hello(to="world"):
#     print("Hello,", to)


# hello()
# name = input("What's your name? ")
# hello(name)


def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    print("hello,", to)


main()
