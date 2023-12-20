# Einstein
# e = mc^2


# Declare a function relativity()
def relativity():
    # Create variable of c (speed of light, m/s)
    c = 300000000

    # Take in user input in kg
    user_input = input("Please enter some mass in kg: ")

    # Convert mass to an integer as a variable m
    m = int(user_input)

    # Formula for energy and variable of e
    e = m * (c**2)

    print(e)


# call function
relativity()

# Test cases:
# 1 should output 90000000000000000
# 14 should output 1260000000000000000
# 50 should output 4500000000000000000

# check50 cs50/problems/2022/python/einstein

# submit50 cs50/problems/2022/python/einstein
