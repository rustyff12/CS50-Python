# Extensions
# Suffixes
# .gif = image/gif
# .jpg = image/jpeg
# .jpeg = image/jpeg
# .png = image/png
# .pdf = application/pdf
# .zip = application/zip
# .txt = text/plain


# Declare a function, main()
def main():
    # Ask user for input, make case and space insensitive
    user_file = input("Please enter the name of a file: ").lower().strip()

    # Variable for empty string
    # new_string = ""

    # If statement to check for instances of specified suffixes
    if ".gif" in user_file:
        print("image/gif")
    elif ".jpg" in user_file or ".jpeg" in user_file:
        print("image/jpeg")
    elif ".png" in user_file:
        print("image/png")
    elif ".pdf" in user_file:
        print("application/pdf")
    elif ".zip" in user_file:
        print("application/zip")
    elif ".txt" in user_file:
        print("text/plain")
    else:
        print("application/octet-stream")


# Call function
main()

# Test cases
# happy.jpg
# document.pdf

# check50 cs50/problems/2022/python/extensions

# submit50 cs50/problems/2022/python/extensions
