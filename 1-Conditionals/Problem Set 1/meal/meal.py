# Meal
# Meal times are as follows and inclusive:
# 7:00 - 8:00 => breakfast time
# 12:00 - 13:00 => lunch time
# 18:00 - 19:00 => dinner time


# Declare main function
def main():
    # Ask user for the time as a sting in input
    time_now = input("What is the time now? ")
    # Check for a leading "0"
    if time_now[0] == "0":
        time_now.replace("0", "")
    # If time is not correctly formatted return to beginning of main
    if ":" not in time_now:
        print("You must enter a valid time format")
        return main()

    # creating a variable and assigning the user input as an argument to the convert function
    converted_time = convert(time_now)

    # if else statement to see if time is in range of specified meal times
    if converted_time >= 7.00 and converted_time <= 8.00:
        print("breakfast time")
    elif converted_time >= 12.00 and converted_time <= 13.00:
        print("lunch time")
    elif converted_time >= 18.00 and converted_time <= 19.00:
        print("dinner time")


# Declare convert function with argument of time
def convert(time):
    # space-sensitive and spit at ":" to create two separate strings in a list
    time_to_list = time.replace(" ", "").split(":")
    # separating hours and minutes by indexing them
    hours = time_to_list[0]
    minutes = time_to_list[1]

    # Turning strings into floats for hours and minutes
    hours_conversion = float(hours)
    minutes_conversion = float(minutes)

    # converting minutes to decimal, hours not needed
    minutes_to_decimal = round(minutes_conversion / 60, 2)

    # returning them as a float and rejoined with a decimal
    time_decimal = hours_conversion + minutes_to_decimal
    return time_decimal


# convert(" 13 :  58")
if __name__ == "__main__":
    main()


# check50 cs50/problems/2022/python/meal

# submit50 cs50/problems/2022/python/meal


# Perhaps ability for 12 hour time
