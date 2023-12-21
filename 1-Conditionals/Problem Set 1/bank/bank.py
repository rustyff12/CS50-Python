# Bank


# In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.


# declare a function, main()
def main():
    # Ask a user for input, called greeting
    greeting = input("Please enter a greeting: ").lower().strip()
    print(greeting)

    # if statement to determine input/output logic
    # .startswith("hello") in case of edge cases where
    if greeting.startswith("hello"):
        print("$0")
        # first letter is "h" but string is not "hello"
    elif greeting[0] == "h" and greeting != "hello":
        print("$20")
    else:
        print("$100")


# call function
main()

# check50 cs50/problems/2022/python/bank

# submit50 cs50/problems/2022/python/bank
