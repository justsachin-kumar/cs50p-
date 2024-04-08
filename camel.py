# take camelcase unput from user

name = input("camelCase: ")

# print snakecase

print("snake_case: ", end="")

# perform a loop on indivisual letter.

for letter in name:

    # identify upper case alphabet

    if letter.isupper():

        # replace uppercse with underscore and lowercase

        print("_" + letter.lower(), end="")

    # otherwise print inputed letters

    else:
        print(letter, end="")

print()
