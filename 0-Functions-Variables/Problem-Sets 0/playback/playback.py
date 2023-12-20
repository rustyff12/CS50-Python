# Playback speed


# create a function called playback
def playback():
    # Create a variable that takes in user input and must be a string
    sentence = input(str("Please enter a sentence: "))
    # Create another variable that uses the replace string method on the sentence
    replace_string = sentence.replace(" ", "...")

    # print the replace_string variable
    print(replace_string)


# Call function
playback()


# Test cases:
# This is CS50
# This is our week on functions
# Let's implement a function called hello

# Expected output should be as follows: "Hello World" => "Hello...World"

# check50 cs50/problems/2022/python/playback
# submit50 cs50/problems/2022/python/playback
