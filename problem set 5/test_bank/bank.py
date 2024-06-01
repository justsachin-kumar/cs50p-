# defining main function

def main():

    # taking arguments from the user

    greetings = input("Greeting:")
    dollar = value(greetings)

    # printng output

    print(f"${dollar}", end="")


# definding value function and applying conditons

def value(greeting):

    greeting = greeting.strip().lower()

    if greeting.startswith("hello"):
        return int(0)
    elif greeting.startswith("h"):
        return int(20)
    else:
        return int(100)


# calling main function
if __name__ == "__main__":
    main()
