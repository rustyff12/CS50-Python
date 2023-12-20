# f-strings - "format string"
# name = input("Whats's your name?")
# Does NOT need $ like JavaScript
# print(f"Hello, {name}")

# Remove outer whitespace from string
# name = name.strip()

# print(f"Hello, {name}")

# Capitalize user's first letter of name
# name = name.capitalize()
# print(f"Hello, {name}")

# Capitalize first letter in each string
# name = name.title()
# print(f"Hello, {name}")

# Chaining string methods
# name = name.strip().title()
# print(f"Hello, {name}")

# Shorter version
name = input("Whats's your name?").strip().title()

# Say hello to user
# print(f"Hello, {name}")

# split users's name into first name and last name
first, last = name.split(" ")
print(f"Hello, {first}")
