# twttr
# In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.


def no_vowels(str):
    vowels = "aeiouAEIOU"
    new_str = ""

    for i in str:
        if i not in vowels:
            new_str += i

    return new_str


def main():
    user_input = input("Input: ")
    print(no_vowels(user_input))


if __name__ == "__main__":
    main()


# Test Cases:
# Twitter => twttr
# Whats's your name? => Wht's yr nm?
# CS50 => CS50

# check50 cs50/problems/2022/python/twttr

# submit50 cs50/problems/2022/python/twttr
