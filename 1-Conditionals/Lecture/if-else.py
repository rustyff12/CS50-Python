# Conditionals allow you, the programmer, to allow your program to make decisions: As if your program has the choice between taking the left-hand road or the right-hand road based upon certain conditions.

# Operators:
# > and < symbols are probably quite familiar to you.
# >= denotes “greater than or equal to.”
# <= denotes “less than or equal to.”
# == denotes “equals, though do notice the double equal sign! A single equal sign would assign a value. Double equal signs are used to compare variables.
# != denotes “not equal to.
# Conditional statements compare a left-hand term to a right-hand term.

# if statement
x = int(input("What's x? "))
y = int(input("What's y? "))

# if, if, if is unefficent and not well designed
if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")


# elif statement
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")


# else statement
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
