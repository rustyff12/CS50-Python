# interpreter


# Declare a function main()
def main():
    # Ask user for expression
    user_expression = input("Expression: ")
    # Turn the expression into a list using replace() to get rid of whitespace and split it at the ","
    new_list = user_expression.replace(" ", ",").split(",")
    # index the ints and opertor and assign them to a variable
    first_int = new_list[0]
    operator = new_list[1]
    second_int = new_list[2]
    # checking operator and do corresponding operation
    if operator == "+":
        plus = float(first_int) + float(second_int)
        print(plus)
    elif operator == "-":
        minus = float(first_int) - float(second_int)
        print(minus)
    elif operator == "*":
        times = float(first_int) * float(second_int)
        print(times)
    elif operator == "/":
        divide = float(first_int) / float(second_int)
        print(divide)


# call function
main()


# Cases:
# 1 + 1
# 2 - 3
# 2 * 2
# 50 / 5

# check50 cs50/problems/2022/python/interpreter

# submit50 cs50/problems/2022/python/interpreter
