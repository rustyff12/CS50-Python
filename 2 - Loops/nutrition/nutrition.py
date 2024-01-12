# Nutrition
# In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the "FDA’s poster for fruits", which is also "available as text". Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.


def main():
    item = input("Item: ")
    fruit = item.lower()

    if fruit == "apple":
        print("Calories: 130")
    elif fruit == "avocado":
        print("Calories: 50")
    elif fruit == "banana":
        print("Calories: 110")
    elif fruit == "cantaloupe":
        print("Calories: 50")
    elif fruit == "grapefruit":
        print("Calories: 60")
    elif fruit == "grapes":
        print("Calories: 90")
    elif fruit == "honeydew melon":
        print("Calories: 50")
    elif fruit == "lemon":
        print("Calories: 15")
    elif fruit == "lime":
        print("Calories: 20")
    elif fruit == "nectarine":
        print("Calories: 60")
    elif fruit == "orange":
        print("Calories: 80")
    elif fruit == "peach":
        print("Calories: 60")
    elif fruit == "pear":
        print("Calories: 100")
    elif fruit == "pineapple":
        print("Calories: 50")
    elif fruit == "plums":
        print("Calories: 70")
    elif fruit == "strawberries":
        print("Calories: 50")
    elif fruit == "sweet cherries" or fruit == "cherries":
        print("Calories: 100")
    elif fruit == "tangerine":
        print("Calories: 50")
    elif fruit == "watermelon":
        print("Calories: 80")


main()

# TesCases:
# Apple  => Calories: 130
# Avocado => Calories: 50
# Cherries => Calories: 100
# Tomato => output nothing


# check50 cs50/problems/2022/python/nutrition

# submit50 cs50/problems/2022/python/nutrition
