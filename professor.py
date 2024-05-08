import random


def main():
    level = get_level()
    score = generate_integer(level)
    print(f"Score:{score}")


def get_level():
    # Prompts the user for  a level, n. If the user does not input 1, 2, or 3, the program should prompt again.
    while True:
        try:
            n = int(input("Level: "))
            if n not in [1, 2, 3]:
                raise ValueError
        except ValueError:
            pass

        else:
            return n


def generate_integer(level):
    # Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
    if level == 1:
        for i in range(10):
            # Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with n digits. No need to support operations other than addition (+).
            try:
                X = random.randint(0, 9)
                Y = random.randint(0, 9)
                Z = X + Y
                W = int(input(f" {X} + {Y} ="))

                p = 0
                while Z != W and p < 2:
                    print("EEE")
                    W = int(input(f" {X} +{Y} ="))
                    p += 1
                if Z != W:
                    print(f" {X} + {Y} = {Z}")
                    return i
            except ValueError:
                pass
        # The program should ultimately output the user’s score: the number of correct answers out of 10.
        return i + 1

    if level == 2:
        for i in range(10):
            try:
                X = random.randint(10, 99)
                Y = random.randint(10, 99)
                Z = X + Y
                W = int(input(f" {X} + {Y} ="))

                p = 0
                while Z != W and p < 2:
                    print("EEE")
                    W = int(input(f" {X} +{Y} ="))
                    p += 1
                if Z != W:
                    print(f" {X} + {Y} = {Z}")
                    return i
            except ValueError:
                pass
        return i + 1

    if level == 3:
        for i in range(10):
            try:
                X = random.randint(100, 999)
                Y = random.randint(100, 999)
                Z = X + Y
                W = int(input(f" {X} + {Y} ="))

                p = 0
                while Z != W and p < 2:
                    print("EEE")
                    W = int(input(f" {X} +{Y} ="))
                    p += 1
                if Z != W:
                    print(f" {X} + {Y}= {Z}")
                    return i
            except ValueError:
                pass
        return i + 1


if __name__ == "__main__":
    main()
