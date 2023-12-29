# camelCase
# Program that promts user for the name of a variable in camelCase and outputs the corresponding name in snake_case. Assume user input will be in camelCase


# Define a function to convert camelCase to snake_case
def convert(camel_cased_string):
    snake_cased_char_list = []

    # Loop through each char in the input string using for loop
    for char in camel_cased_string:
        # Check for uppercase char
        if char.isupper():
            # If char is uppercase, add "_" and lowercase char
            converted_char = "_" + char.lower()
            snake_cased_char_list.append(converted_char)
        else:
            # If not uppercase, leave it as is
            snake_cased_char_list.append(char)

    # Rejoin the separated list of characters back into a string
    snake_cased_string = "".join(snake_cased_char_list)

    # Return the rejoined string
    return snake_cased_string


# Define the main function
def main():
    # Ask the user for input
    camel_cased_string_input = input("camelCase: ")
    # Call the convert function passing in user input as argument/parameter and print to console
    print(convert(camel_cased_string_input))


if __name__ == "__main__":
    main()
# Test Caes:
# name => name
# firstName => first_name
# prefferedFirstName => preffered_first_name


# check50 cs50/problems/2022/python/camel

# submit50 cs50/problems/2022/python/camel
