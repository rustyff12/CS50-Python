# Deep
def main():
    # Ask for user input
    # .lower() and .strip() to be case and space sensitive
    question = (
        input(
            "What is the Answer to the Great Question of Life, the Universe, and Everything? "
        )
        .lower()
        .strip()
    )
    if question == "42" or question == "forty-two" or question == "forty two":
        print("Yes")
    else:
        print("No")


main()

# Test Cases:
# 42
# Forty Two
# forty-two
# 50

# check50 cs50/problems/2022/python/deep

# submit50 cs50/problems/2022/python/deep
