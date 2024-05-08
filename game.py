# import random libary
import random


# define functions
def main():

    x = guess_no()
    check_no(x)


def guess_no():
    # Prompts the user for a level,n. If the user does not input a positive integer, the program should prompt again.
    while True:
        try:
            n = int(input("Level: "))
            if n < 0:
                raise ValueError
        except ValueError:
            pass
        else:
            # Randomly generates an integer between 1 and n, inclusive, using the random module.
            random_txt = random.randint(1, n + 1)
            return random_txt


def check_no(i):
    while True:
        try:
            guess = int(input("Guess: "))
            # Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
            if guess < 0:
                raise ValueError
            # If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
            elif guess < i:
                print("Too Small!")
            # If the guess is larger than that integer, the program should output Too large! and prompt the user again.
            elif guess > i:
                print("Too Large!")
            # If the guess is the same as that integer, the program should output Just right! and exit.
            elif guess == i:
                print("Just right!", end="")
                break
        except:
            pass


if __name__ == "__main__":
    main()
